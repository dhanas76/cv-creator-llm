def refine_resume(user_edits: dict, current_resume: dict) -> dict:
    # Merge user edits into resume
    updated_resume = current_resume.copy()
    updated_resume.update(user_edits)
    return updated_resume
