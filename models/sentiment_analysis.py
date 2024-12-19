# models/sentiment_analysis.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as VaderSentimentAnalyzer
from textblob import TextBlob
from flair.models import TextClassifier
from flair.data import Sentence

class SentimentAnalyzer:
    def __init__(self):
        self.vader_analyzer = VaderSentimentAnalyzer()
        self.flair_classifier = TextClassifier.load('sentiment')

    def analyze_sentiment(self, text):
        if not text.strip(): return {"neutral": 0.5}
        if not text.strip(): return {"neutral": 0.5}
        if not text.strip(): return {"neutral": 0.5}
        vader_score = self.vader_analyzer.polarity_scores(text)['compound']
        textblob_score = TextBlob(text).sentiment.polarity

        sentence = Sentence(text)
        self.flair_classifier.predict(sentence)
        flair_label = sentence.labels[0].value
        flair_score = sentence.labels[0].score if flair_label == 'POSITIVE' else -sentence.labels[0].score

        combined_score = (vader_score + textblob_score + flair_score) / 3

        if combined_score > 0.1:
            return 'positive'
        elif combined_score < -0.1:
            return 'negative'
        else:
            return 'neutral'
