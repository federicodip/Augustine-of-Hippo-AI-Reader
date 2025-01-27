from cltk import NLP

def main():
    input_file_path = "confessions_latin.txt"     # Path to your Latin .txt file
    output_file_path = "confessions_lat_lemmatized.txt"
    
    # Read the Latin text
    with open(input_file_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Initialize the NLP pipeline for Latin
    nlp = NLP(language="lat")
    
    # Analyze (tokenize, tag, lemmatize, etc.)
    doc = nlp.analyze(text)
    
    # Extract the lemmatized forms from the processed words
    lemmatized_words = [word.lemma for word in doc.words]
    
    # Save or print the results
    with open(output_file_path, "w", encoding="utf-8") as out:
        out.write(" ".join(lemmatized_words))
    
    print(f"Lemmatized text saved to '{output_file_path}'")

if __name__ == "__main__":
    main()
