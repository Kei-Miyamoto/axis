import os
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build
from langchain_core.documents import Document

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

def load_google_doc_by_id(service_account_file: str, document_id: str) -> list[Document]:
    creds = service_account.Credentials.from_service_account_file(
        service_account_file,
        scopes=["https://www.googleapis.com/auth/drive.readonly"]
    )
    service = build('drive', 'v3', credentials=creds)

    request = service.files().export_media(fileId=document_id, mimeType='text/plain')
    file_content = request.execute()
    text = file_content.decode('utf-8')

    metadata = {"source": f"google_doc_{document_id}"}
    return [Document(page_content=text, metadata=metadata)]


def main():
    load_dotenv()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    document_id = os.getenv("DOCUMENT_ID")
    service_account_key_path = os.getenv("SERVICE_ACCOUNT_KEY_PATH")

    if not all([google_api_key, document_id, service_account_key_path]):
        raise ValueError(".envファイルに必要な情報が設定されていません。")
    print("--- 1. Googleドキュメントの読み込み ---")

    try:
        documents = load_google_doc_by_id(service_account_key_path, document_id)
        print(f"読み込み完了。{len(documents)}個のドキュメントを読み込みました。")
    except Exception as e:
        print(f"ドキュメントの読み込み中にエラーが発生しました: {e}")
        return

    print("\n--- 2. ドキュメントの分割 ---")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200)
    split_docs = text_splitter.split_documents(documents)
    print(f"ドキュメントを{len(split_docs)}個のチャンクに分割しました。")

    print("\n--- 3. ベクトル化とデータベースへの保存 (オープンソースモデル使用) ---")
    embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-large")
    batch_size = 5
    print(f"最初のバッチ (チャンク 1-{min(batch_size, len(split_docs))}) を処理中...")
    vectorstore = FAISS.from_documents(split_docs[:batch_size], embeddings)

    if len(split_docs) > batch_size:
        for i in range(batch_size, len(split_docs), batch_size):
            batch = split_docs[i:i + batch_size]
            print(f"次のバッチ (チャンク {i + 1}-{i + len(batch)}) を処理中...")
            vectorstore.add_documents(batch)
    print("ベクトルデータベースの作成が完了しました。")

    print("\n--- 4. 質問応答チェーンの作成 ---")
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0, google_api_key=google_api_key)
    retriever = vectorstore.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    print("質問応答の準備ができました。")

    print("\n--- 5. 質問応答を開始します ---")
    print("質問を入力してください（終了するには '終了' と入力）:")

    while True:
        question = input("> ")

        if question.lower() == '終了':
            print("ボットを終了します。")
            break

        if not question.strip():
            continue

        try:
            print("AIが回答を生成中...")
            response = qa_chain.invoke(question)
            print("\n--- 回答 ---")
            print(response.get('result', '回答を取得できませんでした。'))
            print("\n" + "="*50 + "\n")
            print("次の質問をどうぞ:")

        except Exception as e:
            print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()
