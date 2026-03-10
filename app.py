import os
import json
from dotenv import load_dotenv
from groq import Groq  # New Import
from classifier import classify_intent
from router import route_and_respond

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def log_interaction(intent, confidence, message, response):
    log_entry = {
        "intent": intent,
        "confidence": confidence,
        "user_message": message,
        "final_response": response
    }
    with open("route_log.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")

# In app.py
def main():
    print("\n🚀 Groq-Powered Modular Router Active.")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nYou: ").strip()
        if not user_input: continue
        if user_input.lower() in ["exit", "quit"]: break
        
        intent_info = classify_intent(client, user_input)
        
        # Strip override prefix before sending to the expert LLM
        display_message = user_input
        valid_intents = [f"@{i}" for i in ["code", "data", "writing", "career"]]
        
        if user_input.strip().lower().startswith(tuple(valid_intents)):
            # Split off the first word (the @tag) and keep the rest
            display_message = user_input.split(" ", 1)[1] if " " in user_input else user_input
            
        # Pass the clean 'display_message' to the router, but log the original 'user_input'
        reply = route_and_respond(client, display_message, intent_info)
        
        log_interaction(intent_info['intent'], intent_info['confidence'], user_input, reply)
        
        print(f"\n[INTENT: {intent_info['intent'].upper()} | CONF: {intent_info['confidence']}]")
        print(f"Expert: {reply}")

if __name__ == "__main__":
    main()