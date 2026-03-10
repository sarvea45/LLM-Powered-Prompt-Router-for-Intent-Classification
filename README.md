# LLM-Powered Prompt Router

A modular, intent-classification and routing service. This application uses a two-step LLM chain to categorize user requests and delegate them to specialized expert personas.

## 🚀 Features
- **Intent Classification:** Analyzes prompts to categorize them as `code`, `data`, `writing`, `career`, or `unclear`.
- **Confidence Guardrails:** Safely defaults to `unclear` if the LLM's confidence score drops below 0.70.
- **Opinionated Personas:** Routes the prompt to a specific system persona based on the detected intent.
- **Manual Overrides:** Users can force a specific persona by prefixing their prompt (e.g., `@code How do I sort a list?`).

## 📦 Setup & Installation
1. Clone the repository and navigate into the project folder.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   Create a .env file in the root directory based on .env.example and add your Groq API key:

Code snippet
GROQ_API_KEY=gsk_your_api_key_here
💻 How to Run
Interactive CLI Mode:
Run the main application to chat with the router in real-time.

Bash
python app.py
Automated Test Suite:
Run the test script to automatically process 15+ predefined queries across all categories. Results are appended to route_log.jsonl.

Bash
python test_runner.py

---

### 🧹 3. Clean Up `route_log.jsonl` and Git Tracking
Right now, your `.gitignore` has the log file commented out (`# route_log.jsonl`). Let's fix that so you don't commit messy error logs.

1. **Update `.gitignore`**: Open `.gitignore` and remove the `#` so it looks like this:
   ```text
   # Logs
   route_log.jsonl
Clear the Git Cache: Since the file was already tracked, you need to tell Git to "forget" it. Run this in your terminal:

Bash
git rm --cached route_log.jsonl
Wipe the file: Open route_log.jsonl in your editor, delete all the text inside it, and save it as an empty file.

Create an Example File: Create a new file called route_log.jsonl.example and put just one clean, perfect JSON line in it so reviewers see the format without seeing all your test history.