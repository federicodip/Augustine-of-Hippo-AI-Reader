import os
import shutil
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
import gradio as gr

# Load the text from the file
with open("confessions.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split the text into smaller chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=350,
    chunk_overlap=40,
    separators=["\n\n", "\n", ".", ",", "CAPUT"]
)
splits = splitter.split_text(text)
print(f"Split into {len(splits)} chunks.")

# Create the vector database
embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
persist_directory = './docs/chroma'

if os.path.exists(persist_directory):
    shutil.rmtree(persist_directory)

vectordb = Chroma.from_texts(
    texts=splits,
    embedding=embedding,
    persist_directory=persist_directory
)

print(vectordb._collection.count())

# Define the language model and retrieval chain
llm = ChatOpenAI(model_name='gpt-4', temperature=0.15)

template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, and don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible.
{context}
Question: {question}
Helpful Answer:"""

QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"], template=template)

qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectordb.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

def chatbot_response_with_sources(question):
    # Use the query (which could be either original user prompt or the translated one)
    result = qa_chain({"query": question})
    answer = result.get("result", "No response available.")
    source_docs = result.get("source_documents", [])
    sources = "\n\n".join([f"- {doc.page_content}" for doc in source_docs])
    return f"Answer:\n{answer}\n\nSources:\n{sources}"

def translate_to_latin(prompt):
    # Simple prompt for translation
    translate_prompt = f"Translate the following text into Latin:\n\n'{prompt}'"
    # Use the LLM to translate:
    translation = llm.call_as_llm(translate_prompt)
    return translation.strip()

# Build the Gradio interface using Blocks for more customization
with gr.Blocks(title="Saint Augustine AI Librarian") as demo:
    gr.Markdown("# Saint Augustine AI Librarian")
    gr.Markdown("Ask our Librarian a question about Saint Augustine's Confessions. You can also translate your prompt into Latin before submitting.")

    with gr.Row():
        prompt_input = gr.Textbox(label="Your Prompt", placeholder="Ask your question here...")
    
    with gr.Row():
        translate_button = gr.Button("Translate to Latin")
        submit_button = gr.Button("Submit")
    
    output_box = gr.Textbox(label="Answer and Sources", placeholder="The answer and its sources will appear here...")

    # When the user clicks "Translate", we take the prompt, translate it, and put the translated text back into the prompt box.
    translate_button.click(
        fn=translate_to_latin,
        inputs=prompt_input,
        outputs=prompt_input
    )

    # When the user clicks "Submit", we take whatever is currently in the prompt_input (could be translated text), 
    # and run it through the retrieval QA chain.
    submit_button.click(
        fn=chatbot_response_with_sources,
        inputs=prompt_input,
        outputs=output_box
    )

demo.launch()
