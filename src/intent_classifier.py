# src/intent_classifier.py
import json
import re
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

class IntentClassifier:
    def __init__(self, data_path='data/intents.json'):
        self.data_path = data_path
        self.model = None
        self.intents = []
        self.load_data()
        self.train()

    def load_data(self):
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.intents = data['intents']
            print(f"✓ Data loaded: {len(self.intents)} intents")
        except Exception as e:
            print(f"✗ Error loading data: {e}")
            self.intents = []

    def preprocess(self, text):
        # Simple cleaning: lowercase only
        text = text.lower()
        return text

    def train(self):
        if not self.intents:
            print("✗ No intents to train on!")
            return
        
        patterns = []
        labels = []
        
        for intent in self.intents:
            for pattern in intent['patterns']:
                patterns.append(self.preprocess(pattern))
                labels.append(intent['tag'])
        
        print(f"Training on {len(patterns)} patterns...")
        
        self.model = Pipeline([
            ('tfidf', TfidfVectorizer()),
            ('clf', MultinomialNB())
        ])
        
        self.model.fit(patterns, labels)
        print("✓ Model trained successfully!")

    def predict(self, text):
        if not self.model:
            return "unknown", 0
        
        cleaned_text = self.preprocess(text)
        prediction = self.model.predict([cleaned_text])[0]
        confidence = self.model.predict_proba([cleaned_text])[0].max()
        
        return prediction, confidence