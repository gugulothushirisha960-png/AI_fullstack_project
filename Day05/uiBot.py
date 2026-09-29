import ollama
import streamlit as st
st.markdown("### WelCome !! ")

with st.sidebar:
    st.header(":blue[Chat settings]")
    if st.button("Clear chat🗑️"):
        st.session_state.msgs = []
        st.success("chat cleared")
    personalities = {
        "kid 👶🏻" : "Answer the question like u are explaining a 5 year old kid. Give answers in  2 line only",
        "friend " : "Answer the question in friendly . Give answers in 2 lines only"
    }
    personality = st.selectbox("select a personality",personalities.keys())
    uploaded_file=st.file_uploader("upload a text file..")
    try:
        if uploaded_file:
           st.write("File uploaded successfully")
           context=uploaded_file.read().decode("utf-8")
           if st.button("Display"):
               st.text(context)
    except:
        st.error("file not support")
if "msgs" not in st.session_state:
    st.session_state.msgs = []
for msg in st.session_state.msgs:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("You:")
if question:
    st.session_state.msgs.append({
        "role": "user",
        "content": question
    })
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("Thinking..."):
        response = ollama.chat(
            model="llama3.2:3b",
            messages= [
                {"role" : "system","content": "personalities[personality]"}] + st.session_state.msgs)
            
    answer = response["message"]["content"]
    st.session_state.msgs.append({
        "role": "assistant",
        "content": answer
    })
    with st.chat_message("assistant"):
        st.write(answer)