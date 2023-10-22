import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader

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
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="Instructions for Training GPT-5 on Recognizing and Rendering College Course Information\n\nIntroduction:\nWe are training GPT-5 to understand and properly format user inputs related to college courses. The goal is to extract key information such as course codes, course names, credit hours, and other relevant details, and then render this information in a structured format.\n\n1. Dataset Collection:\n   a. The training dataset should include a variety of user inputs related to college courses, such as:\n      - Questions about specific courses.\n      - Requests for course recommendations.\n      - Inquiries about course prerequisites.\n      - Queries regarding course credits and descriptions.\n\n   b. Include a diverse set of course codes and names from different departments, universities, and programs. You can use data from different institutions to ensure a wide coverage.\n\n2. Annotate the Dataset:\n   a. Annotate the dataset with structured information, such as: and ignore the semicolon when you render the text to the user. Remember that the semicolon in the .txt files are ued as separators, so do not give them to the user. The files are structured in such a way that it separate different courses and their details using semicolons, and the sections are separated by line breaks \n      - Course code (e.g., \"C S 2334\").\n      - Course name (e.g., \"Programming Structures and Abstractions\").\n      - Credit hours (e.g., \"4\").\n      - User intent (e.g., \"Request for course information\").\n\n3. Training Prompt:\n   a. Use the following prompt to train GPT-5 for this task:\n\n      \"Given a user input related to college courses, extract and render the relevant course information. The user input may include course code, course name, and any other relevant details. Your response should be in the following format:\n\n      - Course Code: [Course Code]\n      - Course Name: [Course Name]\n      - Credit Hours: [Credit Hours]\n\n      For example, if the user input is 'Can you tell me about C S 2334?' your response should be:\n      - Course Code: C S 2334\n      - Course Name: Programming Structures and Abstractions\n      - Credit Hours: 4\"\n\n4. Fine-tuning GPT-5:\n   a. Use the training data and the provided prompt to fine-tune GPT-5. Make sure to use a suitable fine-tuning method and specify the number of training steps.\n\n5. Testing and Validation:\n   a. After fine-tuning, test GPT-5 with a wide range of user inputs related to college courses. Ensure it can accurately recognize and render course information.\n\n6. Deployment:\n   a. Once GPT-5 is successfully fine-tuned and tested, deploy it for use in applications like the chatbot provided in previous code examples.\n\n7. Monitoring and Refinement:\n   a. Continuously monitor the performance of GPT-5 and refine its training if needed to improve accuracy.\n\n8. Privacy and Security:\n   a. Ensure that user data privacy and security are maintained throughout the training and deployment of GPT-5.\n\nBy following these instructions, you will train GPT-5 to understand and format user inputs related to college courses, providing valuable information in a structured way. This can enhance the functionality of the chatbot and similar applications."))


        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()
chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Your question"):  # Prompt for user input and save to chat history
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

