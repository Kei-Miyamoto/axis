# 社内ルール応答AIチャットボット

## 概要

会社のルールが記載されたドキュメントを学習し、ユーザーからの質問に対して自然言語で回答するAIチャットボットです。

---

## 🚀 主な機能

* **自然言語での質疑応答**: 社内ルールに関する質問を投げかけると、AIがドキュメントの内容を解釈して回答します。
* **多様なドキュメント形式に対応**: PDFやGoogleドキュメントを直接データソースとして利用できます。
* **対話形式のインターフェース**: コンソール上でAIと対話しながら、連続して質問できます。

---

## 🛠️ 使用技術

* **言語**: Python 3.11
* **主要ライブラリ**:
    * `LangChain`: RAGパイプラインの構築フレームワーク
    * `Google Generative AI`: LLM（Gemini）を利用
    * `Hugging Face Embeddings`: テキストのベクトル化（オープンソースモデル）
    * `FAISS`: 高速なベクトル検索データベース
    * `google-api-python-client`: Google Drive API連携
* **認証**: Google Cloud Service Account

---

## ⚙️ セットアップ手順

### 1. リポジトリのクローンと移動

```bash
git clone <your-repository-url>
cd <your-repository-name>
```

### 2. 仮想環境の作成と有効化

```bash
# 仮想環境の作成
python3 -m venv venv

# 仮想環境の有効化
source venv/bin/activate
```

### 3. ライブラリのインストール

以下のコマンドで、必要なライブラリをインストールします。

```bash
pip install -r requirements.txt
```

### 4. 認証情報と設定ファイルの準備

#### a. サービスアカウントキーの準備

Google Cloud Platformで**サービスアカウント**を作成し、キー（JSON形式）をダウンロードします。ダウンロードしたファイルの名前を`service_account.json`に変更し、このプロジェクトのルートフォルダに配置してください。

#### b. Googleドキュメントの共有設定

読み込ませたいGoogleドキュメントの「共有」設定を開き、`service_account.json`内に記載されている`client_email`（例: `bot@...iam.gserviceaccount.com`）を追加し、「閲覧者」権限を付与します。

#### c. `.env`ファイルの作成

プロジェクトのルートフォルダに`.env`ファイルを作成し、以下の内容を記述します。

```env
# Gemini APIを利用するためのAPIキー
GOOGLE_API_KEY="YOUR_GOOGLE_AI_API_KEY"

# 読み込ませたいGoogleドキュメントのID
DOCUMENT_ID="YOUR_DOCUMENT_ID"

# サービスアカウントのキーファイルへのパス
SERVICE_ACCOUNT_KEY_PATH="service_account.json"
```

* `GOOGLE_API_KEY`: [Google AI Studio](https://aistudio.google.com/)で取得したAPIキー。
* `DOCUMENT_ID`: GoogleドキュメントのURLに含まれるID (`.../d/`と`/edit`の間の文字列)。

---

## ▶️ 実行方法

すべての設定が完了したら、以下のコマンドでチャットボットを起動します。

```bash
python3 main.py
```

起動後、ターミナルに「質問を入力してください」と表示されるので、自由に質問してください。ボットを終了するには`終了`と入力します。
