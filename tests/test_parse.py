from parse.jd_parser import parse_job_description
import tempfile

def test_parse_job_description():
    jd_text = "We are hiring an AI Engineer with skills in Python, Docker, and LLMs."
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(jd_text)
        f.seek(0)
        result = parse_job_description(f.name)

    assert result["title"] == "AI Engineer"
    assert "Python" in result["keywords"]
