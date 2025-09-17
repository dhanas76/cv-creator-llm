from generate.doc_generator import generate_resume_doc
from docxtpl import DocxTemplate
import os

def test_generate_resume_doc(tmp_path):
    # Create a dummy template
    template_path = tmp_path / "template.docx"
    doc = DocxTemplate()
    doc.save(template_path)

    resume_content = {
        "summary": "Skilled in Python and Docker.",
        "skills": ["Python", "Docker"]
    }

    output_path = generate_resume_doc(resume_content, str(template_path))
    assert os.path.exists(output_path)
