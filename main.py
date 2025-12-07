# This is my small python automation project
# I am trying to learn how logs are parsed and KPIs are calculated.
# This is not advanced but I tried to keep it simple.

from modules.log_parser import parse_logs
from modules.kpi_analyzer import analyze_kpis
from modules.alert_manager import send_alert
from modules.report_generator import generate_report

print("\n--- Python Automation Toolkit (my practice project) ---\n")

# first I am calling the log parser to read the text file
df = parse_logs()

# now analyzing KPIs (just basic ones)
kpis = analyze_kpis(df)

print("KPI Results:", kpis)

# simple condition to check high latency
# (I don’t know real telecom thresholds, so I used 100ms)
if kpis["p95_latency"] > 100:
    send_alert("Warning: 95th percentile latency is above 100 ms")

# creating the PDF report (very basic report)
generate_report(kpis)

print("\nDone! Report created inside the reports folder.\n")
