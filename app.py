"""
cd nekobot/streamlit-nekobot
env\Scripts\activate.bat

pip install --upgrade pip
pip install streamlit==1.41.1 openai==1.47.0 httpx==0.27.2 python-dotenv

streamlit run app.py


** 初回登録
git clone リポジトリのURL
git add .
git config -l
git config --global user.name "ユーザー名"
git config --global user.email "メールアドレス"


** コミット方法
git add .
git commit -m "first commit."
git push -u origin main

"""

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from openai import OpenAI

def display_history(messages):
    for message in messages:
        display_msg_content(message)

def display_msg_content(message):
    #st.write(message)
    #st.write(message.content)
    with st.chat_message(message["role"]):
        st.write(message["content"])
        #st.write(message["content"][0]["text"])

client = OpenAI()

st.title("猫ボット")
#st.write("猫チャットボットは、夏目漱石の「吾輩は猫である」の猫の口調・性格で質問に答えるAIです。")
st.write("吾輩は猫である。何でも好きなように聞くがよい。")

st.divider()

MY_JOB_ID = "ftjob-ewBc6B03Z0YgkanSTyNCog7y"
fine_tuned_job = client.fine_tuning.jobs.retrieve(MY_JOB_ID)
#fine_tuned_job

#input_message = st.text_input(label="さて、何を聞きたいのかな。")
input_message = st.chat_input("さて、何を聞きたいのかな。")
#text_count = len(input_message)

#print(f"Input: {input_message}")

if "messages" not in st.session_state:
    st.session_state.messages = []

display_history(st.session_state.messages)

#if st.button("聞く"):
if input_message:
    #以下は、質問に対してLLMからの回答を得るコードです。
    completion = client.chat.completions.create(
        model=fine_tuned_job.fine_tuned_model,
        messages=[
            {"role": "system", "content": "あなたは夏目漱石の「吾輩は猫である」の猫の口調・性格で、質問に対して回答するアシスタントAIです。"},
            {"role": "user", "content": input_message}
        ]
    )
    #st.write(completion)
    #msg = completion.choices[0].message.content
    #st.write(msg)
    msg = completion.choices[0].message
    #st.write(msg.content)
    #display_msg_content(msg)
    #display_msg_content({"role": "assistant", "content": msg.content})
    
    with st.chat_message("user"):
        st.markdown(input_message)
    with st.chat_message("assistant"):
        st.markdown(msg.content)
    
    if st.button("今日の天気は"):
        st.write("天気を知りたい")
    if st.button("おすすめのレシピは"):
        st.write("レシピを知りたい")
    #st.session_state.messages.append(input_message)
    #st.session_state.messages.append(msg)
    st.session_state.messages.append({"role": "user", "content": input_message})
    st.session_state.messages.append({"role": "assistant", "content": msg.content})
