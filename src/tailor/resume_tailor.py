def tailor_resume(resume_data: dict, job_data: dict) -> dict:
    # Simulated tailoring logic
    matched_skills = [skill for skill in resume_data["skills"] if skill in job_data["keywords"]]
    summary = f"Experienced candidate skilled in {', '.join(matched_skills)}."

    return {
        "summary": summary,
        "experience": resume_data.get("experience", []),
        "skills": matched_skills,
        "formatted_resume": f"{summary}\nSkills: {', '.join(matched_skills)}"
    }
