import os
import re
from pathlib import Path

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="HireFlow AI", page_icon="🧠", layout="wide")

st.title("🧠 HireFlow AI")
st.subheader("Mini AI-powered recruitment screening assistant")
st.write(
    "Compare a job description with candidate resumes, rank candidates by text similarity, "
    "and generate a structured screening summary. This is a decision-support demo, not an "
    "automated hiring decision system."
)

with st.sidebar:
    st.header("How it works")
    st.markdown(
        "1. Paste a job description.\n"
        "2. Add candidate resume text.\n"
        "3. Run the screening workflow.\n"
        "4. Review match scores and evidence."
    )
    st.caption("Demo uses local TF-IDF similarity; no resume text is uploaded to an external AI API.")

job_description = st.text_area(
    "Job description",
    value="AI Intern with interest in AI automation and recruitment workflows. Skills: Python, APIs, Claude, n8n, workflow automation, data analysis, problem solving.",
    height=140,
)

st.markdown("### Candidate resumes")
default_candidates = [
    ("Candidate A", "Python developer with experience building automation scripts, REST API integrations, data cleaning, and a Streamlit dashboard. Interested in AI tools and recruitment workflow automation."),
    ("Candidate B", "Frontend developer skilled in HTML, CSS, JavaScript, responsive design, and UI testing. Built portfolio websites and landing pages."),
    ("Candidate C", "Computer science student with Python, machine learning, NLP basics, Git, API integration, and a project that ranks resumes against job descriptions. Explored Claude and workflow automation concepts."),
]
candidates = []
for i, (default_name, default_text) in enumerate(default_candidates):
    with st.expander(f"Candidate {i+1}", expanded=(i == 0)):
        name = st.text_input("Candidate label", value=default_name, key=f"name_{i}")
        resume = st.text_area("Resume text", value=default_text, height=100, key=f"resume_{i}")
        candidates.append({"name": name.strip() or f"Candidate {i+1}", "resume": resume.strip()})

with st.expander("➕ Add another candidate"):
    extra_name = st.text_input("Additional candidate label", key="extra_name")
    extra_resume = st.text_area("Additional resume text", height=100, key="extra_resume")
    if extra_name.strip() and extra_resume.strip():
        candidates.append({"name": extra_name.strip(), "resume": extra_resume.strip()})

def keywords(text):
    words = re.findall(r"[A-Za-z][A-Za-z0-9+#.-]{1,}", text.lower())
    stop = {
        "and", "the", "with", "for", "from", "that", "this", "are", "you", "your",
        "our", "will", "have", "has", "was", "were", "into", "using", "use", "who",
        "can", "not", "but", "all", "any", "job", "role", "work", "about", "their"
    }
    return {w for w in words if w not in stop and len(w) > 2}

if st.button("🚀 Run screening workflow", type="primary", use_container_width=True):
    valid = [c for c in candidates if c["resume"]]
    if not job_description.strip():
        st.error("Please enter a job description.")
    elif not valid:
        st.error("Please add at least one resume.")
    else:
        docs = [job_description] + [c["resume"] for c in valid]
        vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        matrix = vectorizer.fit_transform(docs)
        scores = cosine_similarity(matrix[0:1], matrix[1:]).flatten()
        job_terms = keywords(job_description)
        results = []
        for candidate, score in zip(valid, scores):
            resume_terms = keywords(candidate["resume"])
            matched = sorted(job_terms & resume_terms)
            missing = sorted(job_terms - resume_terms)
            results.append({
                "Candidate": candidate["name"],
                "Match score": round(float(score) * 100, 1),
                "Matched terms": ", ".join(matched[:12]) or "No direct keyword overlap found",
                "Terms to verify": ", ".join(missing[:8]) or "No obvious keyword gaps",
                "Resume": candidate["resume"],
            })
        results.sort(key=lambda x: x["Match score"], reverse=True)
        st.success(f"Screening complete: compared {len(results)} candidate(s).")
        st.info("Scores measure text similarity, not candidate quality. Verify skills and evidence manually.")
        st.markdown("### Candidate ranking")
        st.dataframe(
            [{k: v for k, v in r.items() if k != "Resume"} for r in results],
            use_container_width=True,
            hide_index=True,
        )
        st.markdown("### Review notes")
        for rank, result in enumerate(results, start=1):
            with st.expander(f"#{rank} — {result['Candidate']} ({result['Match score']}% text match)"):
                st.write("**Relevant terms found:**", result["Matched terms"])
                st.write("**Terms to verify:**", result["Terms to verify"])
                st.write("**Resume text:**")
                st.write(result["Resume"])
                st.write("**Suggested recruiter action:**")
                st.write(
                    "Review the candidate's project evidence and ask a consistent, job-related "
                    "follow-up question about the skills listed. Do not reject or select someone "
                    "based on this score alone."
                )
        csv = "Candidate,Match score,Matched terms,Terms to verify\n" + "\n".join(
            '"' + r["Candidate"].replace('"', '""') + '",' +
            str(r["Match score"]) + ',"' +
            r["Matched terms"].replace('"', '""') + '","' +
            r["Terms to verify"].replace('"', '""') + '"'
            for r in results
        )
        st.download_button(
            "⬇️ Download screening report (CSV)",
            data=csv,
            file_name="hireflow_screening_report.csv",
            mime="text/csv",
        )

st.divider()
st.caption("Responsible-use note: use only job-related criteria, obtain consent for resume processing, and keep a human recruiter in control.")
