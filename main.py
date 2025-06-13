import os
from modules import virustotal, abuseipdb

# Load indicators from input file
with open('inputs/suspicious_indicators.txt', 'r') as file:
    indicators = [line.strip() for line in file.readlines() if line.strip()]

# Run playbook checks
for indicator in indicators:
    print(f"\n--- Scanning Indicator: {indicator} ---")
    vt_result = virustotal.check_indicator(indicator)
    abuse_result = abuseipdb.check_ip(indicator)

    if vt_result:
        print("[VirusTotal] Indicator flagged.")
    else:
        print("[VirusTotal] No threats found.")

    if abuse_result:
        print("[AbuseIPDB] Malicious activity detected.")
    else:
        print("[AbuseIPDB] Clean or unknown.")
