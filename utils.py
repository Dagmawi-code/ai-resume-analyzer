import pdfplumber
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('stopwords')
from nltk.corpus import stopwords

def extract_text_from_pdf(file):
    with pdfplumber.open(file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text() or ''
    return text

def extract_keywords(text, max_keywords=20):
    stop_words = set(stopwords.words('english'))
    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform([text.lower()])
    keywords = vectorizer.get_feature_names_out()
    keywords = [word for word in keywords if word not in stop_words and len(word) > 2]
    return sorted(list(set(keywords)))[:max_keywords]

def match_keywords(resume_keywords, job_keywords):
    matched = list(set(resume_keywords) & set(job_keywords))
    missing = list(set(job_keywords) - set(resume_keywords))
    score = int((len(matched) / len(job_keywords)) * 100) if job_keywords else 0
    return {
        "matched": matched,
        "missing": missing,
        "score": score
    }
