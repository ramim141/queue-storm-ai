# 🚀 QueueStorm AI

An AI-powered FinTech Support Ticket Analyzer built with Django REST Framework and Google Gemini.

---

# 📌 Overview

QueueStorm AI automatically analyzes customer support tickets and helps support agents by:

- Detecting complaint type
- Matching relevant transactions
- Evaluating supporting evidence
- Routing tickets to the correct department
- Generating AI-powered summaries
- Generating customer-friendly replies
- Detecting duplicate payments
- Supporting English, Bangla and Banglish complaints

---

# ✨ Features

- AI Complaint Classification
- Transaction Matching
- Duplicate Payment Detection
- Evidence Reasoning Engine
- AI Summary Generation (Gemini)
- Customer Reply Generation
- Safety Filtering
- Department Routing
- Confidence Score
- Structured JSON API
- Docker Support
- Logging
- Health Check API

---

# 🛠 Tech Stack

Backend

- Python 3.13
- Django
- Django REST Framework

AI

- Google Gemini 2.5 Flash

Deployment

- Docker
- Docker Compose

---

# 🏗 Architecture

Client

↓

REST API

↓

Serializer Validation

↓

Complaint Analyzer

↓

Duplicate Detector

↓

Transaction Matcher

↓

Evidence Engine

↓

Routing Engine

↓

Prompt Builder

↓

Gemini AI

↓

Safety Engine

↓

Response Builder

↓

JSON Response

---

# 📂 Project Structure

```
queue_storm_ai/

├── api/
├── config/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── README.md
```

---

# ⚙ Installation

Clone repository

```bash
git clone <repository_url>
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

Run

```bash
python manage.py runserver
```

---

# 🐳 Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

---

# 📌 API Endpoints

## Health Check

GET

```
/api/health/
```

---

## Analyze Ticket

POST

```
/api/analyze-ticket/
```

---

## Swagger

```
/api/docs/
```

---

## Redoc

```
/api/redoc/
```

---

# 📥 Sample Request

```json
{
  "ticket_id":"TKT-001",
  "complaint":"I accidentally sent 5000 taka to wrong number.",
  "transaction_history":[
    {
      "transaction_id":"TXN-001",
      "timestamp":"2026-04-14T10:00:00Z",
      "type":"transfer",
      "amount":5000,
      "counterparty":"01712345678",
      "status":"completed"
    }
  ]
}
```

---

# 📤 Sample Response

```json
{
  "ticket_id":"TKT-001",
  "case_type":"wrong_transfer",
  "department":"dispute_resolution",
  "severity":"high",
  "confidence":0.95
}
```

---

# 🔒 Safety

The system never

- Requests OTP
- Requests PIN
- Requests Password
- Promises refunds
- Exposes internal policies

---

# 🌍 Language Support

- English
- Bangla
- Banglish

---

# 🔮 Future Improvements

- OCR Support
- Voice Complaint Analysis
- Fraud Detection Model
- Human Feedback Learning
- Multi-LLM Support

---

# 👨‍💻 Team

QueueStorm AI

Hackathon Submission

2026