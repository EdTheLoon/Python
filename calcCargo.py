#!/usr/bin/python3.6
# Calculate Cargo
# Author: Adrian Reid
# This program calculates the amount of cargo to load or discharge to be
# at the required height out of the water at sea (RWD 1.205)

import os

# INITIALISE GLOBAL VARIABLES
curHeight = 0.0
targetHeight = 0.0
curDensity = 0.0
FWA = 0.0
TPC = 0.0

# Function for clearing the screen
def cls():
	os.system("cls" if os.name == "nt" else "clear")

# Does the calculations
def calcCargo(_curMetres, _targetMetres, _curDensity, _FWA, _TPC):
	_sinkRise = abs(_curMetres - _targetMetres)
	_DWA = (_FWA * ((1025 - _curDensity) / 25)) / 1000
	_totalSinkRise = _sinkRise + _DWA
	_loadDischarge = 100 * (_totalSinkRise * _TPC)
	return _loadDischarge

# Prompts the user for the numbers needed
def getNumbers():
	cls()
	global curHeight, targetHeight, curDensity, FWA, TPC
	curHeight = float(input("Current Draught / Freeboard:\t"))
	targetHeight = float(input("Target Draught / Freeboard:\t"))
	curDensity = float(input("Current density:\t\t"))
	FWA = float(input("FWA:\t\t\t\t"))
	TPC = float(input("TPC:\t\t\t\t"))

# MENU OPTION FUNCTIONS
# OPTION 1
def cargo():
	getNumbers()
	cargoToLoad = calcCargo(curHeight, targetHeight, curDensity, FWA, TPC)
	print("Calculation Result: %.2f tonnes" % cargoToLoad)
	input("Press enter to continue...")
	cls()

# START OF MAIN PROGRAM
# Clear the screen
cls()

# Show the menu and loop until required to exit
inMenu = True
while inMenu:
	print("""1. Calculate cargo to load/discharge
2. Quit""")
	menuR = 0
	menuR = eval(input("Select an option: "))
	if menuR == 1:
		cargo()
	elif menuR == 2:
		print("Quitting...")
		exit()
	else:
		print("Please select a valid menu option")

print("Exit...")
