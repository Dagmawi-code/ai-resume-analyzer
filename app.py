import streamlit as st
from utils import extract_text_from_pdf, extract_keywords, match_keywords
import pdfplumber

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("🤖 AI Resume Analyzer")
st.markdown("Upload your resume and a job description to get feedback.")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if resume_file and job_description:
    with st.spinner("Analyzing resume..."):
        resume_text = extract_text_from_pdf(resume_file)
        resume_keywords = extract_keywords(resume_text)
        job_keywords = extract_keywords(job_description)

        match_result = match_keywords(resume_keywords, job_keywords)
        
        st.subheader("🔍 Results")
        st.write(f"**Keyword Match: {match_result['score']}%**")
        st.write("✅ Matched Keywords:", match_result["matched"])
        st.write("❌ Missing Keywords:", match_result["missing"])
