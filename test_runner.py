import os
import json
from dotenv import load_dotenv
from groq import Groq
from classifier import classify_intent
from router import route_and_respond

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

TEST_MESSAGES = [
    # Code
    "How do I reverse a string in Python?",
    "What is a decorator?",
    "Write a SQL query to find the second highest salary.",
    # Data
    "Explain standard deviation.",
    "How do I find outliers in a dataset?",
    "What does a p-value of 0.03 mean in a t-test?",
    # Writing
    "Check this paragraph for flow.",
    "How do I avoid using 'very' in my essays?",
    "Is my tone too informal for a research paper?",
    # Career
    "How do I prepare for a Java developer interview?",
    "What should go in a LinkedIn headline?",
    "What skills should I learn for a Data Engineering role?",
    # Unclear
    "Hi there!",
    "What's the best movie?",
    "Tell me a joke.",
    # Override Test
    "@code How do I sort a list?"
]

def log_interaction(intent, confidence, message, response):
    log_entry = {
        "intent": intent,
        "confidence": confidence,
        "user_message": message,
        "final_response": response
    }
    with open("route_log.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

# In test_runner.py
def run_tests():
    print("🚀 Starting Automated Test Suite...\n")
    valid_intents = [f"@{i}" for i in ["code", "data", "writing", "career"]]
    
    for msg in TEST_MESSAGES:
        print(f"Processing: '{msg}'")
        intent_info = classify_intent(client, msg)
        
        # Strip prefix logic
        clean_msg = msg
        if msg.strip().lower().startswith(tuple(valid_intents)):
            clean_msg = msg.split(" ", 1)[1] if " " in msg else msg
            
        reply = route_and_respond(client, clean_msg, intent_info)
        log_interaction(intent_info['intent'], intent_info['confidence'], msg, reply)
        print(f"-> Logged as [{intent_info['intent'].upper()}]\n")
    
    print("✅ All tests completed! Check route_log.jsonl for the results.")
if __name__ == "__main__":
    run_tests()