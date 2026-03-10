import json

with open("prompts.json", "r") as f:
    EXPERT_PROMPTS = json.load(f)

def route_and_respond(client, message: str, intent_data: dict) -> str:
    intent = intent_data["intent"]
    
    if intent == "unclear":
        return "I'm not quite sure how to help. Are you asking about coding, data, writing, or career advice?"

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