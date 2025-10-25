# LinkedIn Jobs Pipeline

This repository demonstrates an **end-to-end project**:  
from scraping LinkedIn job postings to cleaning, analyzing, and generating reports.  

It integrates:  
- [linkedin-jobs-scraper](https://github.com/yuliashiyy/linkedin-jobs-scraper)  
- [linkedin-jobs-analysis](https://github.com/yuliashiyy/linkedin-jobs-analysis)  

---

## 🔗 Workflow
    ```mermaid
    flowchart LR
    A[Scraper] --> B[Raw Job Data CSV]
    B --> C[Data Cleaning + Enrichment]
     C --> D[Analysis & Visualizations]
    D --> E[Word Report]

---

📊 Features

Automated scraping with Selenium

Deduplication using job_id

Data cleaning and enrichment (city, work mode, skills extraction)

Exploratory data analysis (EDA)

Competitiveness metric (applications per day)

Visualizations: job distribution, applications histogram, skills demand word cloud

Bilingual Word report (English)


📂 Project Structure

    linkedin-jobs-pipeline/
    │
    ├── scraping/            # Scraper module
    ├── analysis/            # Analysis module
    ├── data/                # Sample datasets only
    ├── report/              # Final Word report
    ├── requirements.txt
    └── README.md

⚙️ Requirements

See requirements.txt for full dependencies.

🚀 Usage

1. Scraping
   ```bash
   cd scraping
   python main.py
  This generates raw job postings into CSV.

2. Analysis
   ```bash
    cd analysis/notebooks
    jupyter notebook analysis.ipynb
  This cleans data, produces visualizations, and generates the report.

3. Outputs

  - Cleaned dataset under /analysis/data/
  
  - Visualizations under /analysis/visualizations/
  
  - Report under /analysis/report/

⚠️ Data Disclaimer

Due to LinkedIn’s Terms of Service, raw scraped data is not shared in this repository.
Instead, we provide a sample dataset for reproducibility, along with the cleaned dataset used in the analysis.

📌 Related Repositories

- [LinkedIn Jobs Scraper](https://github.com/yuliashiyy/linkedin-jobs-scraper)  
- [LinkedIn Jobs Analysis](https://github.com/yuliashiyy/linkedin-jobs-analysis)  









  
