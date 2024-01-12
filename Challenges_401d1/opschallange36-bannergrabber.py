#!/usr/bin/env python3

#     _________
#    / ======= \
#   / __________\
#  | ___________ |
#  | | -       | |
#  | |         | |
#  | |_________| |________________________________
#  \=____________/  	  <Rodrigo Brasil>	  )
#  / """"""""""" \                               /
# / ::::::::::::: \                          =D-'
#(_________________)

# Date created: 12/01/2024
# Last Revision: 12/01/2024
# Purpose: This script performs banner grabbing using Netcat, Telnet, and Nmap by providing a IP or URL and port.
# Note: Scanning using this script can take a while.

# Imported libraries
import subprocess
import socket

def banner_grabbing_nc(target, port):
    print("Performing banner grabbing with Netcat...")
    try:
        # Resolve the domain name to an IP address
        ip_address = socket.gethostbyname(target)
        
        # Use nc with the resolved IP address
        result = subprocess.check_output(['nc', '-v', '-n', ip_address, str(port)], stderr=subprocess.STDOUT, universal_newlines=True)
        print("\nBanner Grabbing with Netcat:")
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"\nError during Netcat banner grabbing: {e.output}")
    except subprocess.TimeoutExpired as e:
        print(f"\nTimeout during Netcat banner grabbing: {e}")
    except socket.gaierror as e:
        print(f"\nError resolving the domain: {e}")

def banner_grabbing_telnet(target, port):
    try:
        result = subprocess.check_output(['telnet', target, str(port)], stderr=subprocess.STDOUT, universal_newlines=True)
        print("\nBanner Grabbing with Telnet:")
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error during Telnet banner grabbing: {e.output}")

def banner_grabbing_nmap(target):
    try:
        result = subprocess.check_output(['nmap', '-p-', '--open', '--script', 'banner', target], stderr=subprocess.STDOUT, universal_newlines=True)
        print("\nBanner Grabbing with Nmap:")
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error during Nmap banner grabbing: {e.output}")

def main():
    target = input("Enter the target URL or IP address: ")
    port = int(input("Enter the target port number: "))

    banner_grabbing_nc(target, port)
    banner_grabbing_telnet(target, port)
    banner_grabbing_nmap(target)

if __name__ == "__main__":
    main()
