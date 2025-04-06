"""
pip install --upgrade pip
pip install streamlit==1.41.1
pip install openai==0.27.8
!pip install openai==1.47.0 httpx==0.27.2

streamlit run app.py
"""

print(f"START") 

import streamlit as st
from openai import OpenAI
client = OpenAI()

print(f"START - NEKO") 

st.title("猫ボット")
#st.write("猫チャットボットは、夏目漱石の「吾輩は猫である」の猫の口調・性格で質問に答えるAIです。")
st.write("吾輩は猫である。何でも好きなように聞くがよい。")

st.divider()

print(f"START - NEKO2") 

MY_JOB_ID = "ftjob-ewBc6B03Z0YgkanSTyNCog7y"
print(f"JOB_ID: {MY_JOB_ID}")
fine_tuned_job = client.fine_tuning.jobs.retrieve(MY_JOB_ID)
print(f"FINE_TUNED_JOB: {fine_tuned_job}")
fine_tuned_job

input_message = st.text_input(label="さて、何を聞きたいのかな。")
text_count = len(input_message)

print(f"Input: {input_message}")

if st.button("聞く"):
    #以下は、質問に対してLLMからの回答を得るコードです。
    print(f"聞く: {input_message}")
    completion = client.chat.completions.create(
        model=fine_tuned_job.fine_tuned_model,
        messages=[
            {"role": "system", "content": "あなたは夏目漱石の「吾輩は猫である」の猫の口調・性格で、質問に対して回答するアシスタントAIです。"},
            {"role": "user", "content": input_message}
        ]
    )
    msg = completion.choices[0].message.content
    st.write(msg)
