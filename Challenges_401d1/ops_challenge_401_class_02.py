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

#Date created: 9/11/2023
#Last Revision: 9/11/2023
#Purpose: Asks for an IP, sends out ICMP packets to the IP and saves the output to a txt file

#Run script with root privilages for better results

#Must have ping3 installed | run on the terminal "pip3 install ping3"

import time
from datetime import datetime
from ping3 import ping, verbose_ping

def check_host_status(target_ip, max_pings = 5):
   for _ in range(max_pings):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')[:-3]

        try:
            response = ping(target_ip, timeout = 1)
            if response is not None:
                status = "Network Active - ICMP received!"
            else:
                status = "Network Inactive - ICMP not received!"

        except Exception as e:
            status = f"Error: {str(e)}"

        log_message = f"{timestamp} {status} to {target_ip}"
        print(log_message)

        with open("uptime_log.txt", "a") as log_file:
            log_file.write(log_message + "\n")

        time.sleep(2)

if __name__ =="__main__":
    
    target_ip = input("Enter the target IP address: ")
    check_host_status(target_ip)
