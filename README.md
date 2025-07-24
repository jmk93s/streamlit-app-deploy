# AI専門家相談アプリ

このアプリは、LangChainとOpenAI GPTを使用して、様々な分野の専門家AIに質問や相談ができるStreamlitアプリケーションです。

## 🚀 機能

- **4つの専門分野**: 医療・健康、IT・プログラミング、ビジネス・経営、心理カウンセリング
- **LangChain統合**: LangChainを使用してLLMとの対話を管理
- **レスポンシブUI**: Streamlitによる直感的なユーザーインターフェース
- **専門家別システムプロンプト**: 選択した専門家に応じたカスタマイズされた回答

## 🛠️ 技術スタック

- **Python 3.11**
- **Streamlit**: Webアプリケーションフレームワーク
- **LangChain**: LLM統合フレームワーク
- **OpenAI GPT-3.5-turbo**: 言語モデル

## 📋 セットアップ

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 2. 環境変数の設定

OpenAI APIキーを設定します：

**ローカル開発の場合：**
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

**Streamlit Community Cloudの場合：**
- アプリ設定のSecretsセクションで `OPENAI_API_KEY` を設定

### 3. アプリの実行

```bash
streamlit run app.py
```

## 🌐 デプロイ

このアプリはStreamlit Community Cloudでのデプロイに最適化されています。
Pythonバージョンは3.11に設定されています（`.python-version`ファイル参照）。

## 📝 使い方

1. 専門家を選択（ラジオボタン）
2. 質問・相談内容を入力
3. 「相談する」ボタンをクリック
4. AI専門家からの回答を受け取る

## 🔧 カスタマイズ

専門家の種類やシステムプロンプトは `app.py` の `get_ai_response` 関数内で変更できます。

## ⚠️ 注意事項

- OpenAI APIキーが必要です
- 医療相談は参考程度に留め、重要な健康問題は医療機関にご相談ください
- 心理的な問題で深刻な場合は、専門機関への相談をお勧めします