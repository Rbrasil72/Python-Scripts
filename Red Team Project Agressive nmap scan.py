#!/usr/bin/env python3

#     _________
#    / ======= \
#   / __________\
#  | ___________ |
#  | | -       | |
#  | |         | |
#  | |_________| |_____________________________________
#  \=____________/   Rodrigo <Sud0Pirat3> Brasil       )
#  / """"""""""" \                                    /
# / ::::::::::::: \                               =D-'
#(_________________)

# Original script made by teammate André Graça later modified by me

# Date created: 01/02/2024
# Last Revision: 01/02/2024
# Purpose: Do an agressive nmap scan for list of pre programed hosts for a Code_for_all Red Team project

import subprocess

def scan_hosts(ip_list, output_file):
    with open(output_file, 'w') as report_file:
        for ip in ip_list:
            report_file.write(f"Scanning {ip}...\n")
            try:
                result = subprocess.run(['nmap','-sV','-A','-O','-v', ip], capture_output=True, text=True, check=True)
                report_file.write(result.stdout)
            except subprocess.CalledProcessError as e:
                report_file.write(f"Error scanning {ip}: {e}\n")

if name == "main":
    ip_list = ['10.0.0.74', '10.0.0.82', '10.0.0.100', '10.0.0.101', '10.0.0.102', '10.0.0.103', '10.0.0.123', '10.0.0.175', '10.0.0.176']
    output_file = 'scan_report.txt'
    scan_hosts(ip_list, output_file)
    print(f"Scan results saved to {output_file}")
