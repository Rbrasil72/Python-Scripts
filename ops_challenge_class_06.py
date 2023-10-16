#!/usr/bin/python3

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

#Date created: 16/10/2023
#Last Revision: 16/10/2023
#Purpose: Output linux commands using python3

#Run script with root privilages for better results

#Imported modules
import os
import subprocess

#Outputs the current user | If ran with root privileges it will output the user as root
print("\033[32mI AM: \033[0m")
whoami = os.system("whoami")

print("\n")

print("..............................................................................")

print("\n")

#Outputs the network interfaces
print("\033[32mNETWORK INTERFACES\033[0m")
showipconfig = os.system("ip a")

print("\n")

print("..............................................................................")

print("\n")

#Outputs information about the hardware configuration
print("\033[32mHARDWARE CONFIGURATION INFORMATION\033[0m")
detailedpcinfo = subprocess.run(["lshw", "-short"])

print("\n")

print("..............................................................................")

print("\n")
