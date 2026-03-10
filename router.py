import json

with open("prompts.json", "r") as f:
    EXPERT_PROMPTS = json.load(f)

def route_and_respond(client, message: str, intent_data: dict) -> str:
    intent = intent_data["intent"]
    
    # Dynamically generate the unclear response using the LLM
    if intent == "unclear":
        system_instruction = (
            "You are a helpful routing assistant. The user asked a question that does not clearly "
            "fall into coding, data analysis, writing, or career advice. Ask them a polite, brief, "
            "and conversational clarifying question to determine which of those 4 areas they need help with."
        )
    else:
        system_instruction = EXPERT_PROMPTS.get(intent)
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Routing Error: {str(e)}"