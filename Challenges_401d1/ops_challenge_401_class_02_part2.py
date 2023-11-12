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

# Date created: 9/11/2023
# Last Revision: 12/11/2023
# Purpose: Asks for an IP, sends out ICMP packets to the IP, saves the output to a txt file and sends the status of the IP to an user given gmail

# User must have a gmail account with twofactorAuthentication on and use the authentication code as the password

# Run script with root privilages for better results

# Must have ping3 installed | run on the terminal "pip3 install ping3"

# Imports
import time
import smtplib
import getpass
from datetime import datetime
from ping3 import ping, verbose_ping
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email Function
def send_email(sender_email, sender_password, recipient_email, subject, body):
    print("Sending email...")
    with smtplib.SMTP('smtp.gmail.com',587) as server:
        try:
            server.starttls()
            server.login(sender_email,sender_password)

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body,'plain'))

            server.sendmail(sender_email, recipient_email, msg.as_string())

            print("Email sent successfully!")

        except Exception as e:
                print(f"Error sending email: {str(e)}")

# ICMP Function
def check_host_status(target_ip, max_pings = 4, email_enabled = False):
    # Input asking for the email credentials
    sender_email = input("Enter your email address: ")
    sender_password = getpass.getpass("Enter yout email password: ")
    recipient_email = input("Enter the admministrator's email address: ")

    prev_status = None

    # checks if the SMTP servers is valid or online
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        try:
            print("Connecting to SMTP server...")
            time.sleep(1)
            print("SMTP Server: 'smtp.gmail.com'")
            print("Port: 587")
        except Exception as e:
            print("Could not find SMTP Server")

    # Makes a scan on the given ip depending on the amount of the variable "max_pings"
    for _ in range(max_pings):
        # gives the current time and date
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')[:-3]
        
        # checks if the ip is active or not
        try:
            response = ping(target_ip, timeout = 1)
            if response is not None:
                status = "Network Status - Active"
            else:
                status = "Network Status - Inactive"

        except Exception as e:
            status = f"Error: {str(e)}"

        log_message = f"{timestamp} {status} to {target_ip}"
        print(log_message)

        # Email structure
        if prev_status is not None and prev_status == status and email_enabled:
            email_subject = "Host Status Change"
            email_body = (
                f"Host status changed!\n"
                f"Previous Status: {prev_status}\n"
                f"Current Status: {status}\n"
                f"Timestamp: {timestamp}\n"
                f"Host: {target_ip}"
            )
        # Creates log file
        with open("uptime_log.txt", "a") as log_file:
            log_file.write(log_message + "\n")

        # In case the user cancels the scan with a keyboard stroke
        prev_status = status
        try:
            time.sleep(2)
        except KeyboardInterrupt:
            print("\nScript interrupted. Closing...")
            break

    # Sends the email
    if email_body and email_enabled:
            send_email(sender_email, sender_password, recipient_email, email_subject, email_body)

if __name__ =="__main__":
    target_ip = input("Enter the target IP address: ")
    check_host_status(target_ip, max_pings = 4, email_enabled = True)
    
