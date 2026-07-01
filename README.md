<a id="top"></a>

# 🌌 ScholarOps Crypto Analytics Pipeline — Day 8 Graduation Project

### An production-grade, modular, end-to-end data engineering pipeline that fetches real-time market data, sanitizes it with Pandas, performs high-speed NumPy array matrix calculations, and outputs automated visual charts and an executive PDF business report.

<p align="center">
  A self-contained data pipeline demonstrating advanced decoupled software design (Fetch → Clean → Analyze → Visualize → Save) without external environment state leaks.
  <br />
  <a href="https://drive.google.com/file/d/1EIW--YJ9F3A4otJbpKsqX2lo1q8n9P8U/view?usp=sharing"><strong>Watch App Demo Video »</strong></a>
  <br />
  <br />
  <a href="https://github.com/attardekhushi78-cpu/UnProf_Pyai_Phase-1-Project">Explore Codebase</a>
  ·
  <a href="https://github.com/attardekhushi78-cpu/UnProf_Pyai_Phase-1-Project/issues">Report Bug</a>
  ·
  <a href="https://github.com/attardekhushi78-cpu/UnProf_Pyai_Phase-1-Project/issues">Request Feature</a>
</p>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#modular-pipeline-architecture">Modular Pipeline Architecture</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#pipeline-execution-matrix">Pipeline Execution Matrix</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
 
  </ol>
</details>

---

## About The Project

This graduation project marks the final capstone completion for **Phase 1 (Python Intermediate)** of the development internship program. Moving away from monolithic script blocks, this software relies on an industry-standard **modular design framework**. 

The pipeline dynamically pulls real-time public assets, validates transactional variables, performs statistical standard deviation assessments, draws presentation charts, and programmatically compiles a print-ready executive PDF document completely from code.

<p align="right">(<a href="#top">back to top</a>)</p>

---

## 🧩 Modular Pipeline Architecture

The application is structured into decoupled, single-responsibility modules to maximize code maintainability and testability:

1. **`main.py` (The Orchestrator):** The central command center that handles initialization, sets up active diagnostic log channels (`app_activity.log`), and sequences data flow cleanly across subsystems.
2. **`data_fetcher.py` (Ingestion Layer):** Safely handles remote network processes to stream real-time JSON payloads from the public CoinGecko market API.
3. **`data_cleaner.py` (Sanitation Layer):** Leverages **Pandas** to isolate tracking indices, normalize token case structures, and deploy `.fillna()` vectors to counter data gaps.
4. **`data_analyzer.py` (Computational Layer):** Passes clean metrics arrays to **NumPy** for high-speed calculation of maximum values, dataset means, and volatility standard deviations (`np.std`).
5. **`data_visualizer.py` (Graphical Layer):** Configures dual-axis visualization layouts with **Matplotlib** to save real-time bar and line distribution charts as static assets.
6. **`pdf_generator.py` (Reporting Layer):** Dynamically builds an executive business document using **ReportLab** layout flowables, embedding generated tables and dashboard graphics perfectly.

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
* [![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
* [![Matplotlib](https://img.shields.io/badge/Matplotlib-📈-blue?style=for-the-badge)](https://matplotlib.org/)
* [![ReportLab PDF](https://img.shields.io/badge/ReportLab-PDF_Engine-red?style=for-the-badge)](https://www.reportlab.com/)

---

## Getting Started

Because this repository strictly follows dependency best practices, you can stand up the entire development environment and run the workspace pipeline locally in moments.

### Prerequisites
* **Python 3.8 or higher** installed on your terminal local shell platform.

### Setup & Run Instructions

# 1. Clone your project repository workspace down from GitHub
git clone    && cd unprof

# 2. Install all external module dependencies with a single command
pip install -r requirements.txt

# 3. Fire up the central orchestrator to launch the full pipeline
python main.py



### 💻 Pipeline Execution Matrix
Executing the main entry script runs the entire data loop and prints clear progress updates directly to your terminal console workspace:

Console Output Screen Log:
Plaintext

⚡ SCHOLAROPS MODULAR DATA PIPELINE SUITE ENGINE RUNNING


🌐 [Fetcher] Initializing connection to data API server...
🧹 [Cleaner] Initializing column filters and text wrangler tools...
📊 [Analyzer] Handing matrix slices to NumPy vectorized math arrays...
📈 [Visualizer] Rendering canvas plots utilizing Matplotlib engines...
📄 [PDF Engine] Programmatically assembling ReportLab file blocks...
🏆 Success! Final report generated cleanly at path: 'reports/Phase1_Final_Execution_Report.pdf'
💾 [Backup Engine] Extracted rows backed up cleanly to path: 'data/crypto_cleansed_records.csv'


🎉 FRAMEWORK RESOLVED: ALL PIPELINE STAGES STEP COMPLETED

Self-Generating Output Tree Architecture:
Plaintext
unprof/
│
├── data/                             # Generated dynamically at runtime
│   └── crypto_cleansed_records.csv   # Sanitized backup tabular file
├── reports/                          # Generated dynamically at runtime
│   └── Phase1_Final_Execution_Report.pdf # Final executive PDF print document
├── visuals/                          # Generated dynamically at runtime
│   └── market_summary_chart.png      # Matplotlib dashboard image asset
│
├── .gitignore                        # Standard tracking filter layout
├── requirements.txt                  # Consolidated package register
├── main.py                           # Application central coordinator
├── data_fetcher.py                   # REST API ingestion handler
├── data_cleaner.py                   # Pandas dataframe wrangler 
├── data_analyzer.py                  # NumPy vector matrix calculations
├── data_visualizer.py                # Matplotlib charting engine
└── pdf_generator.py                  # ReportLab flowable PDF builder


## 🎯 Roadmap
[x] Phase 1 Day 5: Implement advanced conditional Regex processing algorithms.

[x] Phase 1 Day 6 & 7: Build out data analytics and subplots graphing dashboards.

[x] Phase 1 Day 8: Design and deploy a production-grade decoupled modular end-to-end software suite pipeline.

[ ] Phase 2 Day 1: Begin core integration of asynchronous database listeners.
