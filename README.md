# cv-creator-llm

# 🧠 CV Creation using LLMs

A capstone project that leverages open-source Large Language Models (LLMs) to intelligently extract, tailor, and generate resumes based on job descriptions. This system empowers users to create highly targeted, ATS-friendly resumes with minimal manual effort.

---

## 🚀 Features

- 📄 **Resume Parsing**: Extracts structured data from PDF/DOCX resumes.
- 🧾 **Job Description Analysis**: Identifies key skills and requirements.
- 🛠️ **Resume Tailoring**: Aligns resume content with job descriptions using LLMs.
- 🧰 **Document Generation**: Outputs resumes in DOCX or PDF format.
- 🔁 **Revision Loop**: Supports user feedback and iterative refinement.
- ✅ **ATS Compliance Check**: Evaluates keyword density and formatting.

---

## 🧱 Project Structure

cv-creator-llm/ 
├── src/ # Core modules 
├── data/ # Input resumes, job descriptions, templates 
├── config/ # Configuration files 
├── tests/ # Unit tests 
├── notebooks/ # Exploratory LLM prompts and prototyping 
├── docs/ # Architecture and design documentation


---

## 🧑‍💻 Tech Stack

- **Python 3.10+**
- **LangChain**, **LlamaIndex**, **Transformers**
- **Ollama** (for running Gemma 3B locally)
- **pdfplumber**, **python-docx**, **jinja2**
- **Docker** & `docker-compose` for environment setup

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/cv-creator-llm.git
cd cv-creator-llm
pip install -r requirements.txt

docker-compose up
