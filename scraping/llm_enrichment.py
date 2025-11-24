# @Author : Yulia
# @File   : llm_enrichment.py
# @Time   : 2025/10/24 22:06

from openai import OpenAI

client = OpenAI()

def call_llm(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()


def normalize_job_title(title, description):
    prompt = f"""
You are a job title normalization model. Convert the following job title into a standardized English
professional job title, keeping only the core role. Avoid seniority, location, or parentheses.
Return only the final title.

Title: {title}
Description: {description}
"""
    return call_llm(prompt)


def classify_job_category(description):
    prompt = f"""
You are a job classification model. Based on the job description, classify this role into one of the
following categories:

- Data Engineering
- Data Analytics / BI
- Machine Learning / AI
- Software Engineering
- DevOps / Cloud Engineering
- Product Management
- UX / UI

Return only the category name.

Description: {description}
"""
    return call_llm(prompt)


def extract_skills(description):
    prompt = f"""
Extract up to 12 concrete skills from the job description. Focus on tools, programming languages,
frameworks, cloud platforms, and data technologies. Return the result as a JSON list.

Description: {description}
"""
    return call_llm(prompt)

