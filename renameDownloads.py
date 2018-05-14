#!/usr/bin/python3.5
# Script to automatically rename downloaded files so that they are not
# cluttered.

# IMPORTS 
import os
import argparse

# ARGUMENT PARSER
parser = argparse.ArgumentParser(
	description="Remove clutter from filenames.",
	epilog="Be careful to check the printed list for any errors!")
parser.add_argument(
	"-s",
	"--spaces",
	help="-Use this to work with spaces rather than dots in the filename.",
	action="store_true")
parser.add_argument(
	"-f",
	"--file",
	help="-The file(s) to work on. Leave blank to work on entire directory",
	nargs="*")
args = parser.parse_args()
useSpaces = args.spaces
processFiles = []
processFiles = args.file

# GLOBAL VARIABLES
oldFiles = []
newFiles = []


# Function to determine the new filename, removing unwanted characters.
def createFileName(curFile):
	global oldFiles, newFiles
	# Rudimentary, but skip "U.N.C.L.E"
	if curFile.find("U.N.C.L.E") >= 0: 
		return
	newFile = ""
	extIndex = curFile.rfind(".")
	fileExt = curFile[extIndex:]
	workingFile = curFile[0:extIndex]
	if useSpaces:
		fileSplit = workingFile.split(" ")
	else:
		fileSplit = workingFile.split(".")
	
	# If there is no clutter in the filename then move onto next file
	if len(fileSplit) <= 1:
		return
	
	# Loop through the list and remove clutter
	for curSplit in fileSplit:
		if curSplit.find("720") >= 0 or curSplit.find("HD") >= 0 or curSplit.find("hd") >= 0:
			newFile = newFile + "(720p)"
			break
		elif curSplit.find("1080") >= 0:
			newFile = newFile + "(1080p)"
			break
		elif curSplit.find("DVD") >= 0 or curSplit.find("dvd") >= 0 or curSplit.find("480") >= 0:
			newFile = newFile + "(480p)"
			break
		elif len(curSplit) == 4 and curSplit.isdigit() == True:
			continue
		else:
			newFile = newFile + curSplit + " "
	newFile = newFile.rstrip() + fileExt
	oldFiles.append(curFile)
	newFiles.append(newFile)

def renameFiles():
	# Finally, rename the files
	global oldFiles, newFiles
	listLength = len(oldFiles)

	if listLength == 0:
		print("There are no files to rename. Quitting...")
		exit()
	print("Files:")
	for i in range(0, listLength):
		print("    {} ---> {}".format(oldFiles[i], newFiles[i]))

	response=input("Do you really want to rename all these files? Y or N: ")

	if response == "Y" or response == "y":
		for i in range(0, listLength):
			os.rename(oldFiles[i], newFiles[i])
	else:
		print("Files not renamed. Quitting...")
		exit()
		os.rename(oldFiles[i], newFiles[i])

# MAIN RUNNING SEQUENCE
if not processFiles:
	listFiles = os.listdir()
	listFiles.sort()
	for curF in listFiles:
		createFileName(curF)
	renameFiles()
else:
	for curF in processFiles:
		createFileName(curF)
	renameFiles()
