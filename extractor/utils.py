import spacy

def extract_nouns_verbs_from_text(text):
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text with spaCy
    doc = nlp(text)

    # Extract nouns and verbs
    nouns = list(set([token.text for token in doc if token.pos_ == "NOUN"]))
    verbs = list(set([token.text for token in doc if token.pos_ == "VERB"]))

    return nouns, verbs
