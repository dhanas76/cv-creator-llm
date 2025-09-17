from extract.resume_parser import extract_resume_data

def test_extract_resume_data(monkeypatch):
    # Mock pdfplumber output
    class MockPage:
        def extract_text(self):
            return "Name: John Doe\nEmail: john@example.com\n- Python\n- Docker"

    class MockPDF:
        pages = [MockPage(), MockPage()]
        def __enter__(self): return self
        def __exit__(self, *args): pass

    monkeypatch.setattr("pdfplumber.open", lambda _: MockPDF())

    result = extract_resume_data("dummy.pdf")
    assert result["name"] == "John Doe"
    assert result["email"] == "john@example.com"
    assert "Python" in result["skills"]
