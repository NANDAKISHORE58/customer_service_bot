# src/response_engine.py
import json
import random

class ResponseEngine:
    def __init__(self, data_path='data/intents.json'):
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
            self.intents = self.data['intents']
            print(f"✓ Response engine loaded: {len(self.intents)} intents")
        except Exception as e:
            print(f"✗ Error loading response engine: {e}")
            self.intents = []

    def get_response(self, intent_tag):
        for intent in self.intents:
            if intent['tag'] == intent_tag:
                return random.choice(intent['responses'])
        
        return "I'm sorry, I didn't quite understand that. Could you rephrase?"

    def get_fallback_response(self):
        return "I'm not sure I understand. Please try asking about pricing, support, or hours."