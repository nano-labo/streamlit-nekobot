"""
pip install --upgrade pip
pip install streamlit==1.41.1 openai==1.47.0 httpx==0.27.2 python-dotenv

streamlit run app.py
"""

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
from openai import OpenAI
client = OpenAI()

st.title("猫ボット")
#st.write("猫チャットボットは、夏目漱石の「吾輩は猫である」の猫の口調・性格で質問に答えるAIです。")
st.write("吾輩は猫である。何でも好きなように聞くがよい。")

st.divider()

MY_JOB_ID = "ftjob-ewBc6B03Z0YgkanSTyNCog7y"
fine_tuned_job = client.fine_tuning.jobs.retrieve(MY_JOB_ID)
#fine_tuned_job

input_message = st.text_input(label="さて、何を聞きたいのかな。")
text_count = len(input_message)

#print(f"Input: {input_message}")

if st.button("聞く"):
    #以下は、質問に対してLLMからの回答を得るコードです。
    completion = client.chat.completions.create(
        model=fine_tuned_job.fine_tuned_model,
        messages=[
            {"role": "system", "content": "あなたは夏目漱石の「吾輩は猫である」の猫の口調・性格で、質問に対して回答するアシスタントAIです。"},
            {"role": "user", "content": input_message}
        ]
    )
    msg = completion.choices[0].message.content
    st.write(msg)
