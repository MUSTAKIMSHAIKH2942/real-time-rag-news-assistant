
from sentence_transformers import SentenceTransformer
from nltk.tokenize import sent_tokenize

def clean_and_chunk(text):
    sentences = sent_tokenize(text)
    return [" ".join(sentences[i:i+5]) for i in range(0, len(sentences), 5)]
