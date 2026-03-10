# LLM-Powered Prompt Router

A modular, intent-classification and routing service. This application uses a two-step LLM chain to categorize user requests and delegate them to specialized expert personas.

## 🚀 Features
- **Intent Classification:** Analyzes prompts to categorize them as `code`, `data`, `writing`, `career`, or `unclear`.
- **Confidence Guardrails:** Safely defaults to `unclear` if the LLM's confidence score drops below 0.70.
- **Opinionated Personas:** Routes the prompt to a specific system persona based on the detected intent.
- **Manual Overrides:** Users can force a specific persona by prefixing their prompt (e.g., `@code How do I sort a list?`).
- **Full Logging:** Every request is logged to `route_log.jsonl` with intent, confidence, message, and response.

## 📦 Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sarvea45/LLM-Powered-Prompt-Router-for-Intent-Classification.git
   cd LLM-Powered-Prompt-Router-for-Intent-Classification
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file from the example and add your Groq API key:
   ```bash
   cp .env.example .env
   # Then edit .env and set: GROQ_API_KEY=gsk_your_api_key_here
   ```

## 💻 How to Run

**Interactive CLI Mode:**
```bash
python app.py
```

**Automated Test Suite** (runs 16 predefined queries across all categories):
```bash
python test_runner.py
```

**Docker:**
```bash
docker-compose up --build
```

## 🗂️ Project Structure

```
├── app.py            # Main CLI entry point
├── classifier.py     # classify_intent() — LLM-based intent detection
├── router.py         # route_and_respond() — expert persona routing
├── prompts.json      # Expert system prompts (code, data, writing, career)
├── test_runner.py    # Automated test suite with 16 test messages
├── route_log.jsonl   # Auto-generated request log (gitignored)
├── Dockerfile
├── docker-compose.yml
└── .env.example
```

## 🧠 How It Works

```
User Message
    │
    ▼
classify_intent()       ← fast LLM call → {intent, confidence}
    │
    ▼
route_and_respond()     ← selects expert system prompt → final LLM call
    │
    ▼
Response + route_log.jsonl entry
```

## 📋 Supported Intents

| Intent | Persona |
|---|---|
| `code` | Expert programmer — production-ready code, error handling |
| `data` | Data analyst — statistical reasoning, visualization suggestions |
| `writing` | Writing coach — diagnose issues, never rewrites for you |
| `career` | Career advisor — concrete actionable steps, no platitudes |
| `unclear` | Asks a clarifying question to determine which area you need |
