import json

def classify_intent(client, message: str) -> dict:
    clean_message = message.strip()
    
    # 1. Manual Override Logic
    valid_intents = ["code", "data", "writing", "career"]
    for intent in valid_intents:
        if clean_message.lower().startswith(f"@{intent}"):
            return {"intent": intent, "confidence": 1.0}
            
    # 2. LLM Classification Logic
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Return ONLY a JSON object with 'intent' (code, data, writing, career, or unclear) and 'confidence' (0.0 to 1.0)."},
                {"role": "user", "content": clean_message}
            ],
            response_format={"type": "json_object"}
        )
        
        data = json.loads(response.choices[0].message.content)
        
        # Confidence Guardrail 
        if data.get("confidence", 0.0) < 0.70:
            return {"intent": "unclear", "confidence": data.get("confidence", 0.0)}
            
        return data
    except Exception as e:
        return {"intent": "unclear", "confidence": 0.0}