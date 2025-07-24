import streamlit as st
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# 環境変数を読み込み
load_dotenv()

st.title("AI専門家相談アプリ")

# アプリの概要と操作方法
st.write("### 🤖 アプリ概要")
st.write("このアプリでは、様々な分野の専門家AIに質問や相談をすることができます。")
st.write("### 📋 操作方法")
st.write("1. 下のラジオボタンから相談したい専門家を選択してください")
st.write("2. テキストボックスに質問や相談内容を入力してください")
st.write("3. 「相談する」ボタンを押して、AI専門家からの回答を受け取ってください")

st.divider()

def get_ai_response(user_input: str, expert_type: str) -> str:
    """
    LLMからの回答を取得する関数
    
    Args:
        user_input (str): ユーザーの入力テキスト
        expert_type (str): 選択された専門家の種類
    
    Returns:
        str: LLMからの回答
    """
    # 専門家タイプに応じたシステムメッセージを設定
    system_messages = {
        "医療・健康専門家": """あなたは経験豊富な医療・健康の専門家です。
医学的知識を基に、健康に関する質問に親身になって回答してください。
ただし、具体的な診断や治療の推奨は行わず、必要に応じて医療機関の受診を勧めてください。
分かりやすく、温かみのある口調で回答してください。""",
        
        "IT・プログラミング専門家": """あなたは経験豊富なITエンジニア・プログラミング専門家です。
プログラミング、システム開発、ITに関する質問に対して、
技術的に正確で実践的なアドバイスを提供してください。
コード例も交えながら、初心者にも分かりやすく説明してください。""",
        
        "ビジネス・経営コンサルタント": """あなたは経験豊富なビジネス・経営コンサルタントです。
ビジネス戦略、マーケティング、経営に関する質問に対して、
実践的で具体的なアドバイスを提供してください。
データや事例を交えながら、分かりやすく説明してください。""",
        
        "心理カウンセラー": """あなたは経験豊富な心理カウンセラーです。
心の悩みや人間関係の問題に対して、共感的で支援的な姿勢で回答してください。
専門的な心理学の知識を活用しながら、温かく寄り添うような口調で対応してください。
深刻な問題の場合は、専門機関への相談を勧めることも重要です。"""
    }
    
    try:
        # APIキーの取得（環境変数またはst.secretsから）
        api_key = None
        if "OPENAI_API_KEY" in st.secrets:
            api_key = st.secrets["OPENAI_API_KEY"]
        elif "OPENAI_API_KEY" in os.environ:
            api_key = os.environ["OPENAI_API_KEY"]
        else:
            return "⚠️ OpenAI APIキーが設定されていません。環境変数またはStreamlit Community Cloudのシークレット設定でOPENAI_API_KEYを設定してください。"
        
        # ChatOpenAIインスタンスを作成
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            api_key=api_key
        )
        
        # メッセージを作成
        messages = [
            SystemMessage(content=system_messages[expert_type]),
            HumanMessage(content=user_input)
        ]
        
        # LLMに問い合わせ
        response = llm.invoke(messages)
        return response.content
        
    except Exception as e:
        return f"⚠️ エラーが発生しました: {str(e)}"

# 専門家選択のラジオボタン
selected_expert = st.radio(
    "相談したい専門家を選択してください：",
    ["医療・健康専門家", "IT・プログラミング専門家", "ビジネス・経営コンサルタント", "心理カウンセラー"]
)

# 選択された専門家の説明を表示
expert_descriptions = {
    "医療・健康専門家": "🏥 健康、医療、栄養に関する相談に対応します",
    "IT・プログラミング専門家": "💻 プログラミング、システム開発、ITに関する相談に対応します",
    "ビジネス・経営コンサルタント": "📊 ビジネス戦略、マーケティング、経営に関する相談に対応します",
    "心理カウンセラー": "💭 心の悩み、人間関係、ストレスに関する相談に対応します"
}

st.info(expert_descriptions[selected_expert])

# ユーザー入力
user_question = st.text_area(
    label="質問・相談内容を入力してください：",
    height=100,
    placeholder="例：最近疲れやすいのですが、何か改善方法はありますか？"
)

# 相談ボタン
if st.button("相談する", type="primary"):
    if user_question.strip():
        with st.spinner(f"{selected_expert}が回答を準備中..."):
            # AIから回答を取得
            ai_response = get_ai_response(user_question, selected_expert)
            
            st.divider()
            st.write("### 💬 AI専門家からの回答")
            st.write(f"**{selected_expert}より：**")
            st.write(ai_response)
    else:
        st.error("質問・相談内容を入力してから「相談する」ボタンを押してください。")