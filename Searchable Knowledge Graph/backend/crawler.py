import requests
from bs4 import BeautifulSoup
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities_from_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    text = soup.get_text()

    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
