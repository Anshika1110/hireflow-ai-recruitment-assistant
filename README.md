# HireFlow AI — Recruitment Screening Assistant

A small, runnable AI-assisted recruitment workflow demo. It compares a job description with candidate resume text, ranks candidates using TF-IDF cosine similarity, shows overlapping/missing terms for recruiter review, and exports a CSV report.

## Features
- Job description input
- Candidate resume text input
- Resume-to-job text similarity ranking
- Matched terms and terms to verify
- CSV export
- Local processing: resume text is not sent to an external AI API
- Human-in-the-loop and responsible-use reminders

## Tech stack
- Python
- Streamlit (interactive web UI)
- scikit-learn (TF-IDF vectorization and cosine similarity)
- Regular expressions (simple keyword extraction)
- Git/GitHub (version control and project sharing)

## AI / automation tools
- **Implemented AI/NLP method:** TF-IDF text vectorization with cosine similarity for candidate-to-job-description matching.
- **Workflow automation:** the “Run screening workflow” action performs comparison, ranking, evidence display, and report generation in one flow.
- **Claude:** Claude can be used as a development assistant to brainstorm, review, and improve the workflow. This repository does not claim a live Claude API integration.

## Run locally
1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (optional but recommended).
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   streamlit run app.py
   ```
6. Open the local URL printed in the terminal, usually `http://localhost:8501`.

## Quick demo
The app includes sample job-description and resume text. Click **Run screening workflow** to see the ranking and export a CSV. Replace the examples with fictional or consented candidate data for a demo.

## Limitations and responsible use
- Similarity scores are not probabilities of success and do not measure a person's overall ability.
- Keyword overlap can miss equivalent skills and context.
- Do not use demographic, protected, or irrelevant personal information to rank candidates.
- Keep a human recruiter responsible for decisions; validate results consistently.
- This is a portfolio prototype, not a production-ready hiring platform. Production use would require security, access controls, privacy review, evaluation, monitoring, and integration testing.

## Possible next steps
- Parse uploaded PDF/DOCX resumes
- Add a real Claude API integration with secure server-side secrets and explicit consent
- Connect an n8n/Make workflow through a webhook
- Add authentication, audit logs, tests, and deployment
