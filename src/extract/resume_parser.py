import pdfplumber
import re

def extract_resume_data(file_path: str) -> dict:
    with pdfplumber.open(file_path) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())

    # Simple regex-based extraction (can be replaced with LLM)
    name = re.search(r"Name:\s*(.*)", text)
    email = re.search(r"Email:\s*(.*)", text)
    skills = re.findall(r"-\s*(\w+)", text)

    return {
        "name": name.group(1) if name else "Unknown",
        "email": email.group(1) if email else "Unknown",
        "skills": skills,
        "raw_text": text
    }
