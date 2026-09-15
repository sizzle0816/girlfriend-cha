import streamlit as st
import random as rd
import time

# 定数
QUESTIONS = [
    "それでそれで？",
    "ほかには？",
    "ねぇねぇ、聞いてよ",
    "うんうん！",
    "ってことは...?"
]
REPLIES = [
    "へーそうなんだ",
    "すごーい（棒）",
    "ま？",
    "ウケる笑",
    "ふ～ん",
    "ほんまかいなぁ",
    "そっかそっかぁ",
    "感謝するっ！",
    "{user_msg}なんだね",
    "お疲れさまだよぉ",
    "{user_msg}...ってコト！？",
    "{user_msg}"
]

st.title("彼女とのチャットアプリ")

# セッション初期化
if "chat" not in st.session_state:
    st.session_state.chat = []  # [{'role':'user'|'bot','text':...}, ...]
if "last_reply" not in st.session_state:
    st.session_state.last_reply = None
if "last_ques" not in st.session_state:
    st.session_state.last_ques = None

# 名前入力（終了はチャット入力で行う）
name = st.text_input("彼女の名前：", value="彼女")
if name.strip() == "":
    name = "彼女"

# チャット表示
for msg in st.session_state.chat:
    role = msg.get("role")
    text = msg.get("text")
    if role == "user":
        st.markdown(f"**You:** {text}")
    else:
        st.markdown(f"**{name}:** {text}")

# 入力フォーム（1つに統一）
with st.form(key="chat_form", clear_on_submit=True):
    user_msg = st.text_input("You：", key="input_text")
    submitted = st.form_submit_button("送信")

if submitted and user_msg:
    user_msg_clean = user_msg.strip()
    # 終了判定
    if user_msg_clean.lower() == 'q':
        st.success("チャットを終了します。")
        st.session_state.chat.append({"role": "user", "text": user_msg_clean})
        st.experimental_rerun()

    # ユーザーメッセージを保存して表示
    st.session_state.chat.append({"role": "user", "text": user_msg_clean})

    # 直前と異なる返信を選ぶ
    available_replies = [r for r in REPLIES if r != st.session_state.last_reply]
    chosen_reply = rd.choice(available_replies)
    # 安全にユーザーメッセージを埋め込む
    safe_reply = chosen_reply.replace("{user_msg}", user_msg_clean)

    # 直前と異なる質問を選ぶ
    available_questions = [q for q in QUESTIONS if q != st.session_state.last_ques]
    chosen_ques = rd.choice(available_questions)

    st.session_state.last_reply = chosen_reply
    st.session_state.last_ques = chosen_ques

    # タイピング演出（短時間）
    with st.spinner(f"{name}が入力中..."):
        time.sleep(rd.uniform(0.6, 1.5))

    st.session_state.chat.append({"role": "bot", "text": safe_reply})
    st.session_state.chat.append({"role": "bot", "text": chosen_ques})
    st.experimental_rerun()
