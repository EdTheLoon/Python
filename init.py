#!/usr/bin/python3.5
# Initialisation Script
# Run as root using sudo ie 'sudo ./init.py'

# IMPORTS
import os

# Change to Scripts directory
os.chdir("Scripts/")

# Mount the Window filesystem
osRes = os.system("sh mount.sh")

# Update the system
osRes = os.system("sh update-all.sh")

# Connect to VPN
osRes = os.system("sh vpn.sh CZ1")

print("[init.py] Script completed.")
