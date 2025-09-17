from docxtpl import DocxTemplate

def generate_resume_doc(resume_content: dict, template_path: str) -> str:
    doc = DocxTemplate(template_path)
    context = {
        "summary": resume_content["summary"],
        "skills": ", ".join(resume_content["skills"]),
    }
    doc.render(context)
    output_path = "output/resume.docx"
    doc.save(output_path)
    return output_path
