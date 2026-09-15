import streamlit as st
import random as rd
import time

st.title("彼女とのチャットアプリ")

st.write("終わるにはQまたはqを押してねっ")
name = st.text_input("彼女の名前：")
if name:
	st.write(f"{name}：やっほー")
name_killed = None
if name:
	if name.lower() == 'q':
		st.write("人だね、殺します")
		name_killed = name
		name = "激オコの我"
	else:
		st.write("どしたん？")
question = [
    "それでそれで？",
    "ほかには？",
    "ねぇねぇ、聞いてよ",
    "うんうん！",
    "ってことは...？"
]
replies = [
    "へーそうなんだ",
    "すごーい（棒）",
    "ま？",
	"ふ～ん"
    "{user_msg}...ってコト！？",
    "{user_msg}"
]
##########################################################
# 前回の返信を保存
if "last_reply" not in st.session_state:
    st.session_state.last_reply = None
if "last_ques" not in st.session_state:
    st.session_state.last_ques = None
# メッセージ入力
user_msg = st.chat_input("You：", key="chat_input")
if user_msg:
  # 前回と異なる返信を選ぶ
  available_replies = [
    r for r in replies
    if r != st.session_state.last_reply
  ]
  chosen_reply = rd.choice(available_replies)
  chosen_reply = chosen_reply.format(user_msg=user_msg)
  st.session_state.last_reply = chosen_reply
  # 前回と異なる質問を選ぶ
  available_questions = [
    q for q in question
    if q != st.session_state.last_ques
  ]
  chosen_ques = rd.choice(available_questions)
  st.session_state.last_ques = chosen_ques
#########################################################
  if user_msg.lower() == 'q':
    if not name_killed:
      st.write("また来てねっ")
    else:
      st.write("優しくしてりゃキューキューいいやがって\n二度とその汚ねぇツラ見せんなよっ")
    st.stop()
  else:
    st.write("既読")
    typing_time = rd.uniform(2.0, 5.0)
    time.sleep(typing_time)

  if name_killed:
    st.write(f"{name} : {chosen_reply}（圧）")
    st.write(f"{name} : {chosen_ques}（圧）")
  else:
    st.write(f"{name} : {chosen_reply}")
    st.write(f"{name} : {chosen_ques}")
