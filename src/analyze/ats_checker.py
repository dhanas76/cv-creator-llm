def analyze_ats_compliance(resume_text: str, job_keywords: list) -> dict:
    matched = [kw for kw in job_keywords if kw in resume_text]
    score = int((len(matched) / len(job_keywords)) * 100)

    return {
        "score": score,
        "missing_keywords": list(set(job_keywords) - set(matched)),
        "format_issues": []
    }
