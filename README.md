# Augustine-of-Hippo-AI-Reader
![picture](https://github.com/user-attachments/assets/b3c23916-1aa7-4c43-aa0e-618554b1c783)

**Augustine of Hippo AI Reader** is a Generative AI-powered application that allows users to explore and retrieve information from the philosophical works of Saint Augustine of Hippo, one of the most influential thinkers of all time. The app combines advanced AI techniques with an accessible interface to enable both casual users and scholars to delve into Augustine's profound ideas.

## Features

- **Ask Questions in Plain Language**: Non-specialists can ask questions in natural language and receive concise, contextually accurate answers.
- **Translate Prompts to Latin**: Scholars can translate their questions into Latin, ensuring consistency with Augustine's original philosophical vocabulary.
- **Augmented Retrieval**: Combines cutting-edge retrieval-augmented generation (RAG) to provide relevant answers, supported by source citations from the original text.
- **Interactive Interface**: A user-friendly Gradio-based interface makes it simple to query the app and interact with Augustine's works.

## How It Works

1. **Text Preprocessing**: Augustine's text is split into manageable chunks using a recursive text splitter to ensure effective retrieval.
2. **Vector Embeddings**: The chunks are embedded into a vector database using OpenAI’s embeddings model.
3. **Query Handling**:
   - Users can input their questions in plain English or translate them into Latin for more precise results.
   - The application uses a RetrievalQA chain with a GPT-4 language model to find and present the most relevant information.
4. **Output**: The app generates concise answers and lists sources from Augustine’s works to support the response.

## Requirements

To run this application, you need the following:

- Python 3.8 or higher
- An OpenAI API key
- Required Python packages (listed in `requirements.txt`)



