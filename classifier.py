import json

def classify_intent(client, message: str) -> dict:
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Return ONLY a JSON object with 'intent' (code, data, writing, career, or unclear) and 'confidence' (0.0 to 1.0)."},
                {"role": "user", "content": message}
            ],
            response_format={"type": "json_object"}
        )
        
        data = json.loads(response.choices[0].message.content)
        
        # Confidence Guardrail (Requirement 4 & 6)
        if data.get("confidence", 0.0) < 0.70:
            return {"intent": "unclear", "confidence": data.get("confidence", 0.0)}
            
        return data
    except Exception as e:
       
        return {"intent": "unclear", "confidence": 0.0}