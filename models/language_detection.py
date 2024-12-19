# models/language_detection.py
from langdetect import detect

class LanguageDetector:
    def __init__(self):
        pass

    def detect_language(self, text):
        try:
            language = detect(text)
            return language
        except:
            return 'unknown'
