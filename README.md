# 🛡️ AI-Shield Sentinel: End-to-End Secure LLM Gateway

AI-Shield is a containerized microservices architecture designed to protect Large Language Models (LLMs) from **Adversarial Prompt Injections** and **Jailbreak attacks**. 

This project bridges the gap between **AI/ML Research** and **Cybersecurity Engineering**, providing a secure middleware layer that sanitizes and validates user prompts before they reach the inference engine.

## 🚀 Key Features
- **Security Sentinel:** FastAPI-based backend that uses heuristic analysis to detect malicious prompt patterns (e.g., Payload Splitting, DAN-mode, and System Overrides).
- **Microservices Architecture:** Orchestrated using Docker Compose, featuring isolated Frontend, Backend, and Database layers.
- **Threat Intelligence:** Every blocked attack is persisted to a **PostgreSQL** database for forensic auditing and trend analysis.
- **M2 Optimized:** Specifically configured for Apple Silicon (ARM64) high-performance containerization.

## 🛠️ Tech Stack
- **Frontend:** Streamlit (Python)
- **Backend:** FastAPI (Asynchronous Python)
- **Database:** PostgreSQL 15
- **Infrastructure:** Docker & Docker Compose
- **Security Logic:** Regular Expression Heuristics & Input Sanitization

## 📸 Architecture


## 🚦 How to Run (M2 Mac)
1. **Clone the repo:**
   ```bash
   git clone git@github.com:Pradyum-1712/AI-Shield-Sentinel.git
   cd AI-Shield-Sentinel
   ```
2. **Launch the stack:**
   ```bash
   docker compose up --build
   ```
3. **Access the Gateway:**
   - Frontend: http://localhost:8501
   - API Docs: http://localhost:8000/docs

## 🧠 Academic Connection
This project implements security principles discussed in my published research (IJRAR/Springer) regarding data integrity and adversarial patterns in machine learning environments.
