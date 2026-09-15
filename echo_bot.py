import streamlit as st
import random as rd
import time

st.title("彼女とのチャットアプリ")

st.write("終わるにはQまたはqを押してねっ")
name = st.text_input("彼女の名前：")
st.write(f"{name}：やっほー")
name_killed = None
if name.lower() == 'q':
  st.write("人だね、殺します")
  name_killed = name
  name = "激オコの我"
else:
  st.write("どしたん？")

user_msg = st.text_input("\nYou : ", key="chat_input")

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

last_reply = None
last_ques = None

chosen_reply = rd.choice(replies)
chosen_ques = rd.choice(question)

if user_msg:
  available_replies = [r for r in replies if r != last_reply]
  chosen_reply = rd.choice(available_replies).format(user_msg=user_msg)
  last_reply = chosen_reply

  available_questions = [q for q in question if q != last_ques]
  chosen_ques = rd.choice(available_questions)
  last_ques = chosen_ques

  if user_msg.lower() == 'q':
    if name_killed.lower() != 'q':
      st.write("また来てねっ")
    else:
      st.write("優しくしてりゃキューキューいいやがって\n二度とその汚ねぇツラ見せんなよっ")
    st.stop()
  else:
    st.write("既読")
    typing_time = rd.uniform(2.0, 5.0)
    time.sleep(typing_time)
    if name_killed != None:
      st.write(f"{name} : {chosen_reply}（圧）")
      st.write(f"{name} : {chosen_ques}（圧）")
    else:
      st.write(f"{name} : {chosen_reply}")
      st.write(f"{name} : {chosen_ques}")
  user_msg = st.text_input("\nYou : ", key="chat_input")
