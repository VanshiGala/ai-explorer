#  AI Web Search Agent (Gemini 2.5 Flash + FastAPI + Tavily)

An AI-powered backend agent that performs **live web search and intelligent response generation** using:

-  Tavily Search API (real-time web results)
-  Google Gemini 2.5 Flash (LLM reasoning)
-  FastAPI (high-performance backend)

The system acts as a lightweight **AI research assistant** capable of answering queries using real-time internet data.

---

#  System Architecture

```text
User Prompt
    ↓
FastAPI Endpoint (/ask)
    ↓
Tavily Web Search API
    ↓
Top Search Results (context)
    ↓
Gemini 2.5 Flash LLM
    ↓
Reasoned Response Generation
    ↓
JSON Response to Client
```

---

#  Features

-  Real-time web search integration
-  AI-powered reasoning using Gemini 2.5 Flash
-  FastAPI async backend
-  Lightweight modular architecture
-  Secure API key management via `.env`
-  Structured JSON API responses
-  Prompt orchestration layer for LLM context building

---

#  Project Structure

```text
ai_agent/
│
├── main.py            # FastAPI server + routes
├── agent.py           # AI orchestration logic
├── search.py          # Tavily search wrapper
├── requirements.txt   # Dependencies
├── .env               # API keys (not committed)
└── README.md
```

---

#  Tech Stack

### Backend
- Python 3.10+
- FastAPI
- Uvicorn

### AI + Search
- Gemini 2.5 Flash (Google Generative AI)
- Tavily Search API

### Libraries
- fastapi
- uvicorn
- google-generativeai
- tavily-python
- python-dotenv

---

#  Installation Guide

## 1️. Clone Repository

```bash
git clone https://github.com/VanshiGala/ai-explorer.git
cd ai-agent
```

---

## 2️. Create Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️. Install Dependencies

```bash
pip install -r requirements.txt
```

---

#  Environment Variables

Create a `.env` file:

```env
GEMINI_KEY=your_gemini_api_key
TAVILY_KEY=your_tavily_api_key
```

### API Keys:
-  Gemini: https://aistudio.google.com/
-  Tavily: https://tavily.com/

---

#  Running the Project

Start server:

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

#  API Reference

##  POST /ask

### Request

```json
{
  "prompt": "Give me recipe for pulav"
}
```

---

### Response

```json
{
  "success": true,
  "answer": "Step-by-step pulav recipe with ingredients..."
}
```

---

# Execution Flow

```text
POST /ask
    ↓
main.py (FastAPI route)
    ↓
agent.run_agent()
    ↓
search.search_web()
    ↓
Tavily API (web results)
    ↓
Prompt construction
    ↓
Gemini 2.5 Flash processing
    ↓
Final AI response
    ↓
JSON output
```

---

#  Agent Design

### Core Logic

1. Accept user query
2. Fetch relevant web results
3. Inject results into prompt context
4. Send to Gemini LLM
5. Return structured response

---

#  Example Queries

```text
Give me recipe for pulav

Best places to visit in Mumbai

Latest AI news today

Explain blockchain in simple terms

How to make paneer butter masala

Top frontend frameworks in 2026
```

Current system:

```text
Search + Prompt Engineering + LLM
```

Built with:

```text
Python + FastAPI + Gemini 2.5 Flash + Tavily API
```
