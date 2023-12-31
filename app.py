import pandas as pd
import streamlit as st
from streamlit_chat import message
import tempfile
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import ConversationalRetrievalChain
from langchain.chains import RetrievalQA
from langchain.chains.summarize import load_summarize_chain
from langchain.chains import AnalyzeDocumentChain

DB_FAISS_PATH = "vectorstore/db_faiss"

# Loading the model
@st.cache_resource(show_spinner="Loading model...")
def load_llm(use_llm, temperature=0.1):
    # Load the locally downloaded model here
    if use_llm == "Llama 2 7B Chat":
        llm = CTransformers(
            model="llama-2-7b-chat.ggmlv3.q8_0.bin",
            model_type="llama",
            max_new_tokens=256,
            temperature=temperature,
        )
    elif use_llm == "Llama 2 13B Chat":
        llm = CTransformers(
            model="llama-2-13b-chat.ggmlv3.q8_0.bin",
            model_type="llama",
            max_new_tokens=256,
            temperature=temperature,
        )
    elif use_llm == "Open Llama 3B v2":
        llm = CTransformers(
            model="open-llama-3b-v2-q4_0.bin",
            model_type="llama",
            max_new_tokens=256,
            temperature=temperature,
        )
    elif use_llm == "Mamba GPT-3B":
        llm = CTransformers(
            model="mamba-gpt-3b-v3.ggmlv3.q4_0.bin",
            model_type="llama",
            max_new_tokens=256,
            temperature=temperature,
        )
    return llm

st.set_page_config(
    page_title="Talk to your csv data",
    page_icon="🗄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

col1, col2 = st.columns([3,1])

with col1:
    element_status = st.sidebar.info('Inicializando aplicação...', icon="📟")

def status(message, icon="⏳"):
    element_status.info(message, icon=icon)

with col1:
    st.title("Chat with CSV using Llama2 🦙🦜")

use_llm = st.sidebar.selectbox(
    "Model",
    [
        "Open Llama 3B v2",
        "Llama 2 7B Chat",
        "Llama 2 13B Chat",
        "Mamba GPT-3B",
    ],
    index=0,
    key="use_llm",
)

method_type = st.sidebar.selectbox(
    "Method",
    [
        "Conversational",
        "QA",
    ],
    index=0,
    key="method_type",
)

uploaded_file = st.sidebar.file_uploader("Upload your Data", type="csv")

cpu_type = st.sidebar.selectbox(
    "CPU",
    [
        "cpu",
        "cuda",
    ],
    index=0,
    key="cpu_type",
)

temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.1,
    max_value=1.0,
    value=0.1,
    key="temperature",
    step=0.1
)

st.sidebar.write('# Example Question \nWhich actor made the movie with worse rating?')
st.sidebar.markdown("Built by [AI Anytime](https://github.com/AIAnytime) with ❤️")
st.sidebar.markdown("Changed by [MarceloXP](https://github.com/marceloxp) with 🤪")

if uploaded_file:
    status('Carregando arquivo...')
    # use tempfile because CSVLoader only accepts a file_path
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name

    loader = CSVLoader(
        file_path=tmp_file_path, encoding="utf-8", csv_args={"delimiter": ","}
    )
    data = loader.load()

    with col2:
        df = pd.read_csv(tmp_file_path)
        st.write('## Data uploaded')
        st.write(df[:25])
    
    status('Lendo embedding...')
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": cpu_type},
    )

    status('Carregando banco de dados...')
    db = FAISS.from_documents(data, embeddings)
    db.save_local(DB_FAISS_PATH)

    status('Carregando modelo...')
    llm = load_llm(use_llm, temperature)
    status('Definindo conversational chain...')
    retriever=db.as_retriever()
    if method_type == "QA":
        chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())
    else:
        chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever)

    def query(query):
        status('Procesando mensagem...')
        if method_type == "QA":
            result = chain(query)
            text = result["result"]
        else:
            result = chain({"question": query, "chat_history": st.session_state["history"]})
            text = result["answer"]
        status('Resposta recebida')
        st.session_state["history"].append((query, text))
        return text

    if "history" not in st.session_state:
        st.session_state["history"] = []

    if "generated" not in st.session_state:
        st.session_state["generated"] = [
            "Hello ! Ask me anything about " + uploaded_file.name + " 🤗"
        ]

    if "past" not in st.session_state:
        st.session_state["past"] = ["Hey ! 👋"]

    with col1:
        # container for the chat history
        response_container = st.container()
        # container for the user's text input
        container = st.container()

        with container:
            with st.form(key="my_form", clear_on_submit=True):
                user_input = st.text_input(
                    "Query:", placeholder="Talk to your csv data here (:", key="input"
                )
                submit_button = st.form_submit_button(label="Send")

            if submit_button and user_input:
                output = query(user_input)
                st.session_state["past"].append(user_input)
                st.session_state["generated"].append(output)

        if st.session_state["generated"]:
            with response_container:
                for i in range(len(st.session_state["generated"])):
                    message(
                        st.session_state["past"][i],
                        is_user=True,
                        key=str(i) + "_user",
                        avatar_style="no-avatar",
                    )
                    message(
                        st.session_state["generated"][i], key=str(i), avatar_style="no-avatar"
                    )
else:
    with col2:
        st.info('No data uploaded', icon="🚳")

status('Aplicação pronta!', icon="✅")