from tailor.resume_tailor import tailor_resume

def test_tailor_resume():
    resume_data = {"skills": ["Python", "Docker", "Excel"]}
    job_data = {"keywords": ["Python", "Docker", "LLM"]}

    result = tailor_resume(resume_data, job_data)
    assert "Python" in result["skills"]
    assert "Docker" in result["skills"]
    assert "Excel" not in result["skills"]
    assert "Experienced candidate" in result["summary"]
