#!/usr/bin/python3.5
# A program to calculate the standard deviation and other data options

# IMPORTS
import os
import statistics
import math

# GLOBAL VARIABLES
dataL 		= [0.0]
dataMean 	= 0.0
dataMode 	= 0.0
dataMedian 	= 0.0
dataMin		= 0.0
dataMax		= 0.0
dataRange	= 0.0
dataSum		= 0.0
dataSumSq	= 0.0
dataStanDev = 0.0
dataNum		= 0

def getSampleData():
	global dataL, dataNum
	dataL = []
	cls()
	print("Please enter each sample. Press enter after each one. Enter 'q' when all data is entered")
	userQuit = False
	userIn = input()
	while userQuit == False:
		if userIn.find("q") >= 0 or userIn.find("Q") >= 0:
			userQuit = True
			break
		else:
			try:
				dataL.append(float(userIn))
			except Exception:
				print("You entered a non-numerical value. Please try again")
			finally:
				userIn = input()
	dataNum = len(dataL)
	
def sortData():
	global dataL
	dataL.sort()

def calcMean():
	global dataL, dataMean
	#global dataL, dataNum, dataMean
	#sum = 0
	#for i in range(0,dataNum-1):
	#	sum = sum + dataL[i]
	#dataMean = sum / dataNum
	dataMean = statistics.mean(dataL)
	print("The mean is: {:.3f}".format(dataMean))
	input("Press enter to continue... ")
	
def calcMedian():
	global dataL, dataMedian
	dataMedian = statistics.median(dataL)
	print("The median is: {}".format(dataMedian))
	input("Press enter to continue... ")
	
def calcMode():
	global dataL, dataMode
	dataMode = statistics.mode(dataL)
	print("The mode is: {}".format(dataMode))
	input("Press enter to continue... ")
	
def calcStandardDeviation():
	global dataL, dataStanDev, dataSum, dataSumSq
	
	# Calculate sum of x
	dataSum = 0.0
	for num in dataL:
		dataSum = dataSum + num
	
	# Calculate sum of x squared
	dataSumSq = 0.0
	for num in dataL:
		dataSumSq = dataSumSq + (num * num)
	
	# Calculate standard deviation
	#dataStanDev = statistics.pstdev(dataL) THIS IS THE EXACT SAME AS BELOW
	dataStanDev = math.sqrt((dataSumSq - ((dataSum * dataSum) / dataNum)) / dataNum)
	
	print("Sum x:\t\t\t{}".format(dataSum))
	print("Sum x(squared):\t\t{}".format(dataSumSq))
	print("Standard deviation:\t{}".format(dataStanDev))
	input("Press enter to continue... ")
	
def displayMinMaxRange():
	global dataL, dataMin, dataMax, dataRange
	dataMin = min(dataL)
	dataMax = max(dataL)
	dataRange = abs(dataMin - dataMax)
	print("Min:\t{}".format(dataMin))
	print("Max:\t{}".format(dataMax))
	print("Range:\t{}".format(dataRange))
	input("Press enter to continue... ")
	

### PLACE ALL CODE ABOVE MENU BLOCK ####################################
### START OF MENU BLOCK ################################################
def cls():
	os.system("cls" if os.name == "nt" else "clear")

def menuPrompt():
	# Loop the menu until the quit option is chosen
	menuR = 1
	while menuR != 0:
		# Clear screen and display menu options
		cls()
		print ("""1. Enter sample data
2. Sort data
3. Display data
4. Display number of samples
5. Display min, max and range
6. Calculate mean
7. Calculate median
8. Calculate mode
9. Calcuate standard deviation
0. Exit
-------------------------------""")
		try:
			menuR = eval(input("Please select an option: "))
		except Exception:
			print("Invalid selection. Please press enter to continue...".format(menuR))
		else:
			if menuR == 1: # GET SAMPLE DATA
				getSampleData()
			elif menuR == 2: # SORT DATA NUMERICALLY
				sortData()
				input("Data sorted... Press enter to continue... ")
			elif menuR == 3: # DISPLAY DATA
				print(dataL)
				input("Press enter to continue... ")
			elif menuR == 4: # DISPLAY NUMBER OF SAMPLES
				print("Number of samples: {}".format(dataNum))
				input("Press enter to continue... ")
			elif menuR == 5: # DISPLAY MIN, MAX AND RANGE
				displayMinMaxRange()
			elif menuR == 6: # CALCULATE MEAN
				calcMean()				
			elif menuR == 7: # CALCULATE MEDIAN
				calcMedian()
			elif menuR == 8: # CALCULATE MODE
				calcMode()
			elif menuR == 9: # CALCULATE STANDARD DEVIATION
				calcStandardDeviation()
			elif menuR == 0:
				print("Quitting...")
				exit()
### END OF MENU BLOCK ##################################################

# Call the menu
menuPrompt()
