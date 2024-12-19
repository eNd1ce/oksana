from razdel import tokenize
# utils/preprocessing.py
import re
import emoji
import nltk
import spacy
import stanza

nltk.download('punkt')
spacy_nlp = spacy.load('ru_core_news_sm')
stanza.download('ru')
stanza_nlp = stanza.Pipeline('ru')

def preprocess_message(message):
    message = emoji.replace_emoji(message, replace='')
    tokens_nltk = [t.text for t in tokenize(message)]
    doc_spacy = spacy_nlp(message)
    lemmas_spacy = [token.lemma_ for token in doc_spacy]
    doc_stanza = stanza_nlp(message)
    lemmas_stanza = [word.lemma for sent in doc_stanza.sentences for word in sent.words]
    combined_tokens = list(set(tokens_nltk + lemmas_spacy + lemmas_stanza))
    preprocessed_message = ' '.join(combined_tokens)
    return preprocessed_message
