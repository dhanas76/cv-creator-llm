def parse_job_description(file_path: str) -> dict:
    with open(file_path, "r") as f:
        jd_text = f.read()

    # Simulated keyword extraction
    keywords = [kw for kw in ["Python", "LLM", "Docker", "NLP"] if kw in jd_text]

    return {
        "title": "AI Engineer",
        "keywords": keywords,
        "raw_text": jd_text
    }
