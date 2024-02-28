from langchain_community.llms import Ollama
import streamlit as st
import os

st.set_page_config(page_title="AI Chatbot")


class chatBot:

    def __init__(self, model="phi"):
        self.llm = Ollama(
            base_url="http://poc-chatbot-ollama-1:11434",
            model=model
        )
        self.response = ""

    def ask(self, prompt: str):
        return st.write_stream(self.llm.stream(prompt))


def chatroom():
    st.title("Ollama Powered Chatbot")
    st.header("ChatRoom")

    if len(st.session_state) == 0:
        model = os.environ.get("LLM_MODEL", "phi")
        st.session_state.chatbot = chatBot(model)
        st.session_state.prompts = []
        st.session_state.answers = []
        with st.chat_message("assistant"):
            st.write("Hello! How can I assist you today ? :balloon:")

    for i in range(len(st.session_state.prompts)):
        with st.chat_message("user"):
            st.markdown(st.session_state.prompts[i])
        with st.chat_message("assistant"):
            st.markdown(st.session_state.answers[i])


    if prompt := st.chat_input("What's up ?"):
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.prompts.append(prompt)

        with st.chat_message("assistant") , st.spinner("Thinking..."):
            answer = st.session_state.chatbot.ask(prompt)
            st.session_state.answers.append(''.join(answer))


if __name__ == "__main__":
    chatroom()
