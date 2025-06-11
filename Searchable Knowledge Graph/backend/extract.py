import spacy
import fitz  # PyMuPDF

nlp = spacy.load("en_core_web_sm")

def extract_entities_from_pdf(file):
    doc = fitz.open(stream=file.file.read(), filetype="pdf")
    text = "\n".join([page.get_text() for page in doc])

    doc_nlp = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc_nlp.ents]
    return entities
