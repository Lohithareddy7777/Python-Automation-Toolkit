# Python Automation Toolkit (Beginner Student Project)

This is a small Python project I made to practice automation and basic data processing.  
The idea is to read a log file, extract some values like latency and throughput,  
calculate simple KPIs, and then generate a PDF report.

I am still learning, so the project is simple and easy to understand.

---

## What this project does
1. Reads network log values from a text file  
2. Calculates:
   - average latency  
   - 95th percentile latency  
   - average jitter  
   - average throughput  
3. Shows an alert if latency looks too high  
4. Creates a simple PDF file with the results  

---

## How to run it

Install the required libraries:

pip install -r requirements.txt


Then run:

python main.py


A PDF report will be created inside the `reports` folder.

---

## Files I created

- `main.py` – main script that runs everything  
- `modules/log_parser.py` – reads and extracts data  
- `modules/kpi_analyzer.py` – calculates KPIs  
- `modules/alert_manager.py` – prints alerts  
- `modules/report_generator.py` – makes a PDF file  
- `data/sample_logs.txt` – sample network logs  

---

## Why I made this
I wanted to practice:
- Python scripting  
- reading files  
- simple data analysis  
- automation  
- making a report file  



