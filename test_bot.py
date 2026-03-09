# test_bot.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.intent_classifier import IntentClassifier
from src.response_engine import ResponseEngine

# Test the model
classifier = IntentClassifier()
engine = ResponseEngine()

test_queries = [
    "Hi",
    "Hello",
    "How much does it cost",
    "I need help",
    "When are you open",
    "Bye"
]

print("=" * 50)
print("TESTING INTENT CLASSIFIER")
print("=" * 50)

for query in test_queries:
    intent, confidence = classifier.predict(query)
    response = engine.get_response(intent) if confidence > 0.4 else "Fallback"
    print(f"\nQuery: '{query}'")
    print(f"Intent: {intent}")
    print(f"Confidence: {confidence:.2f}")
    print(f"Response: {response}")

print("\n" + "=" * 50)
print("TEST COMPLETE")
print("=" * 50)