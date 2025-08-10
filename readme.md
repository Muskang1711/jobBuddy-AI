# 🤖 JobBuddy-AI

JobBuddy-AI is an AI-powered tool that helps match resumes with job descriptions using embeddings and machine learning models.

---

## 🚀 Tech Stack
- **Python**
- **FastAPI**
- **Sentence Transformers** (Embeddings)
- **Scikit-learn**
- **Docker**
- **GitHub Actions** (CI/CD)

---

## 📂 Project Structure
.github/workflow/
└── ci.yaml # CI/CD pipeline
src/
├── convert_all_to_txt.py # Converts PDFs/Docs to text
├── embedding_generator.py# Generates embeddings
├── main.py # FastAPI app entry point
├── model.py # ML model definition
├── schema.py # Request/response schemas
├── test_matcher.py # Unit tests
├── train_model.py # Model training script
dockerfile # Docker build instructions
requirements.txt # Python dependencies
readme.md # Project documentation

yaml
Copy
Edit

---

## 🛠️ How to Run Locally
```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
API Docs → http://localhost:8000/docs

🐳 Run with Docker
bash
Copy
Edit
docker build -t jobbuddy-ai .
docker run -p 8000:8000 jobbuddy-ai
⚙️ CI/CD
This project uses GitHub Actions for automated testing and deployment (.github/workflow/ci.yaml).

✨ Features
Resume → Text conversion

Embedding generation for semantic search

ML-based job-resume matching

FastAPI backend with interactive docs

Author: Muskan Goyal
License: MIT
