import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader
import prompt
from llama_index.memory import ChatMemoryBuffer

openai.api_key = "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"
st.title("The Ultimate OU Advisor for CS majors")
if "messages" not in st.session_state:
    st.session_state.messages = []

if "messages" in st.session_state.keys():
    if len(st.session_state.messages) > 100:  # Limit the number of messages to the last 100
        st.session_state.messages = st.session_state.messages[-100:]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # Create a separate list to store chat history


@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading the data."):

        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt=prompt.prompt))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

memory = ChatMemoryBuffer.from_defaults(token_limit=1500)
index = load_data()
chat_engine = index.as_chat_engine(chat_mode="context", memory=memory, system_prompt=prompt.prompt, verbose=True)

# Prompt for user input and save to chat history
if prompt := st.chat_input("Your question"):
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Display the chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # If last message is not from the assistant, generate a new response
    if st.session_state.chat_history and st.session_state.chat_history[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = chat_engine.chat(prompt)
                st.write(response.response)
                message = {"role": "assistant", "content": response.response}
                st.session_state.chat_history.append(message)
