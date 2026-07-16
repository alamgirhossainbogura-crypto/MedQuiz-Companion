# 🩺 MedQuiz Companion
> **An AI-powered Smart Learning Workspace & Clinical Simulation Platform for Medical and Nursing Students.**

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/Powered%20By-OpenAI%20LLM-orange.svg)](https://openai.com/)

MedQuiz Companion is a production-ready, interactive educational workspace built for the **OpenAI Build Week Hackathon**. It directly solves the critical challenge that medical and nursing students face: mastering overwhelming healthcare terminologies and experiencing realistic clinical environments before stepping into real-life hospital wards.

🔗 **Live Demo URL:** `YOUR_REPLIT_DEPLOYMENT_URL_HERE`

---

## 🏗️ System Architecture & Data Flow

The application follows a clean, modular Model-View-Controller (MVC) pattern utilizing Python Flask for the backend and a highly responsive Bootstrap 5 interface for the frontend.

mermaid
graph TD
    A[Frontend: Bootstrap 5 + JS] -->|JSON API Request| B[Backend: Flask Core]
    B --> C[src/routes.py]
    C --> D[src/openai_service.py]
    D -->|Context & Context Injection| E[OpenAI API Server]
    E -->|AI Inference Response| D
    D -->|Structured JSON Object| C
    C -->|Asynchronous Data Update| A

  ---

## 🌟 Key Features & Advanced Prompt Engineering

​1. 🎭 Patient Simulator (Clinical Roleplay)
​Allows students to practice history-taking, vital analysis, and diagnostic workflows in a safe, simulated environment.
​Prompt Engineering Design:
​"You are a patient in a simulated clinical environment. Roleplay as this person: [Case Details]. Stay in character at all times. Respond to the medical student's questions briefly, emotionally, and naturally as a sick patient would."

​2. 📚 Study Simplifier (Memory Booster)
​Leverages advanced language models to distill dense medical literature, drug mechanisms (Pharmacology), and anatomical structures into structural highlights and custom mnemonics.
​Prompt Engineering Design:
​"You are an expert medical professor. Simplify the provided medical text into intuitive bullet points, clear actionable explanations, and construct a highly creative mnemonic to memorize it permanently."

​3. 📝 NCLEX Mock Test Generator (Smart Rationales)
​Generates high-yield, scenario-based multiple-choice questions aligned with global NCLEX standards. It dynamically evaluates student performance and prints an explicit clinical rationale.
​Prompt Engineering Design:
​"You are an expert NCLEX board examiner. Generate ONE highly challenging, scenario-based MCQ about [Topic] with 4 options (A, B, C, D). Provide the exact correct answer and a highly detailed clinical Rationale explaining the core pathophysiology behind correct and incorrect options."
 
 
​
## 🔌 API Endpoints Documentation
​POST /api/chat
​The centralized stateful engine powering the Simulator, Simplifier, and Mock Test modules.
​Request Header:
​Content-Type: application/json

## ​Request Body Schema:

{
  "message": "Hello, I am your nurse today. Can you describe your chest pain?",
  "system_prompt": "You are a patient in a simulated clinical environment...",
  "history": [
    {"role": "assistant", "content": "Hello nurse, I feel terrible."}
  ]
}

## Success Response (200 OK):
{
  "success": true,
  "reply": "It feels like a heavy elephant is sitting right on the middle of my chest..."
}


## 🛡️ Medical Disclaimer & Safety Compliance
​NB: This application is strictly powered by Artificial Intelligence for educational, training, and simulation purposes only. It does not provide real-world clinical advice, medical diagnoses, or definitive treatment protocols.
## ​🛠️ Tech Stack & Architecture Details
​Core Backend Framework: Python 3.10+ & Flask (Modular Blueprints Setup)
​Frontend Layer: Responsive HTML5, CSS3, JavaScript Async-Fetch API, Bootstrap 5 UI Component Framework
​State & Context Management: Client-Side Async History Arrays & Dynamic Backend Wrapper
​Security & Infrastructure: Replit Secrets Token Management (Zero Hardcoded Keys Vulnerability)
## ​🚀 Installation & Local Environment Setup
1.Clone the Production Repository:
 git clone [https://github.com/alamgirhossainbogura-crypto/MedQuiz-Companion.git](https://github.com/alamgirhossainbogura-crypto/MedQuiz-Companion.git)
cd MedQuiz-Companion

2.Initialize Virtual Environment & Install Dependencies:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

3.Configure Environment Variables:
Create a .env file in the root directory or register in Replit Secrets:
OPENAI_API_KEY=your_secured_openai_api_key_here

4.Boot Up the Server:
python run.py


## The application will become locally available at http://localhost:8080.
