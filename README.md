# HireFlow AI - Recruitment Screening Assistant

## About the Project

I made this project to explore how AI and automation can be used in the recruitment process. Usually, recruiters have to go through multiple resumes to find candidates whose skills match a job description. I wanted to make a simple application that could help with the initial screening process.

The application compares a job description with different resumes and shows which resumes have more text in common with the job requirements. It also displays matching keywords and lets the user download the results as a CSV file.

## What does it do?

* Takes a job description as input.
* Allows users to enter candidate resume details.
* Compares resumes with the job description.
* Shows a match score for each candidate.
* Displays matching keywords and skills that may need further checking.
* Ranks candidates based on their text similarity scores.
* Generates a CSV report that can be downloaded.

## Technologies Used

* **Python** - Main programming language.
* **Streamlit** - Used to create the web application.
* **scikit-learn** - Used for text processing and similarity calculation.
* **TF-IDF and Cosine Similarity** - Used to compare resumes with the job description.
* **Git and GitHub** - Used to manage and share the project.

## How does it work?

First, the user enters a job description and the resumes they want to compare.

The application converts the text into numerical features using TF-IDF. It then uses cosine similarity to calculate how similar each resume is to the job description.

After that, it displays the scores, matching keywords, and terms that may need to be checked by the recruiter. The results can also be downloaded as a CSV file.

I used sample resumes in the application so that its working can be tested easily.

## How to Run the Project

1. Install Python on your computer.

2. Download or clone this repository.

3. Open the project folder in VS Code.

4. Open the terminal and install the required libraries:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   streamlit run app.py
   ```

6. Open the local address displayed in the terminal.

## AI and Automation

The project uses basic NLP techniques to compare resumes and job descriptions. The screening workflow runs with one button click and automatically calculates scores, ranks the resumes, displays keyword matches, and creates a downloadable report.

I built this as a small project to understand how AI-based text analysis can be used in a real-world recruitment workflow.

## Limitations

This is a basic project, so there is still room for improvement. The scores are based on text similarity and do not necessarily indicate whether someone is suitable for a job. The results should only help with initial screening, and the final decision should always be made by a recruiter.

## Future Improvements

* Allow users to upload PDF resumes directly.
* Explore integration with Claude for resume analysis.
* Connect the application with an automation tool such as n8n.
* Improve the matching logic to understand skills and experience in more detail.
* Add more testing and features to make the application more reliable.
