from analyze.ats_checker import analyze_ats_compliance

def test_analyze_ats_compliance():
    resume_text = "Experienced in Python and Docker."
    job_keywords = ["Python", "Docker", "LLM"]

    result = analyze_ats_compliance(resume_text, job_keywords)
    assert result["score"] == 66
    assert "LLM" in result["missing_keywords"]
