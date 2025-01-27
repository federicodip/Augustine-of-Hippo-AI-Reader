# Augustine-of-Hippo-AI-Reader
![picture](https://github.com/user-attachments/assets/b3c23916-1aa7-4c43-aa0e-618554b1c783)

**Augustine of Hippo AI Reader** is a Generative AI-powered application that allows users to explore and retrieve information from the philosophical works of Saint Augustine of Hippo—one of the most influential thinkers of all time. The app combines advanced AI techniques with an accessible interface to enable both casual users and scholars to delve into Augustine's profound ideas.

---

## Features

1. **Ask Questions in Plain Language**  
   Non-specialists can ask questions in natural language and receive concise, contextually accurate answers.

2. **Translate Prompts to Latin**  
   Scholars can translate their questions into Latin, ensuring consistency with Augustine’s original philosophical vocabulary.

3. **Augmented Retrieval**  
   Combines cutting-edge retrieval-augmented generation (RAG) to provide relevant answers, supported by source citations from the original text.

4. **Interactive Interface**  
   A user-friendly Gradio-based interface makes it simple to query the app and interact with Augustine’s works.

5. **Topic Modeling and Text Analysis**  
   Utilize TF-IDF vectorization and Latent Dirichlet Allocation (LDA) to uncover dominant themes within Augustine’s text, helping users identify and explore key topics.

6. **Location Mapping of Ancient Places**  
   Read a list of ancient locations mentioned in Augustine’s works, match them with geographical coordinates from a CSV file, and generate an interactive Folium map to visualize these historical sites.

7. **Latin Text Lemmatization**  
   Use a CLTK-based pipeline to process the original Latin text, performing tokenization, tagging, and lemmatization for deeper linguistic and morphological analysis.

---

## How It Works

1. **Text Preprocessing**  
   - Augustine’s text is split into manageable chunks using a recursive character text splitter to ensure effective retrieval.  
   - For deeper analysis, TF-IDF vectorization and LDA modeling are applied to these chunks to identify underlying themes.

2. **Vector Embeddings**  
   - The text chunks are embedded into a vector database using OpenAI’s embeddings model, enabling fast and relevant similarity searches.

3. **Query Handling**  
   - Users can input questions in plain English or translate them into Latin for precise results aligned with the original philosophical context.  
   - The application uses a RetrievalQA chain with a GPT-4 language model to find and present the most relevant information.  
   - Responses include concise answers and a list of sources from Augustine’s works.

4. **Geospatial Visualization**  
   - Ancient place names drawn from Augustine’s text are mapped to coordinates stored in a CSV file.  
   - Folium is used to generate an interactive map, allowing users to visualize and explore historical locations mentioned in the works.

5. **Latin Lemmatization**  
   - A dedicated script leverages the CLTK NLP toolkit to read and process Latin text.  
   - Lemmatized output aids in more accurate linguistic research and advanced text processing tasks.

---

## Requirements

- **Python 3.8 or higher**  
- **An OpenAI API key**  
- **Required Python packages** (listed in `requirements.txt`) including:  
  - `langchain`, `openai`, `gradio` (core application)  
  - `pandas`, `scikit-learn`, `nltk`, `matplotlib` (for topic modeling and text analysis)  
  - `folium` (for interactive maps)  
  - `cltk` (for Latin text lemmatization)

---

With these new functionalities—topic modeling, interactive mapping, and Latin text lemmatization—**Augustine of Hippo AI Reader** provides an even richer toolkit for exploring, analyzing, and visualizing Augustine’s timeless works.



