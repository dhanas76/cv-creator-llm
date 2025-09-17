from extract.resume_parser import extract_resume_data
from parse.jd_parser import parse_job_description
from tailor.resume_tailor import tailor_resume
from generate.doc_generator import generate_resume_doc
from analyze.ats_checker import analyze_ats_compliance
from refine.revision_loop import refine_resume
import yaml

def load_config():
    with open("config/settings.yaml", "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()

    resume_path = f"{config['paths']['resume_input_dir']}sample_resume.pdf"
    jd_path = f"{config['paths']['jd_input_dir']}sample_jd.txt"
    template_path = f"{config['paths']['template_dir']}{config['resume_generation']['template_file']}"

    resume_data = extract_resume_data(resume_path)
    job_data = parse_job_description(jd_path)
    tailored_resume = tailor_resume(resume_data, job_data)
    ats_report = analyze_ats_compliance(tailored_resume['formatted_resume'], job_data['keywords'])

    output_file = generate_resume_doc(tailored_resume, template_path)
    print(f"Resume generated: {output_file}")
    print(f"ATS Score: {ats_report['score']}")

if __name__ == "__main__":
    main()
