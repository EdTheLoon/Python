#!/usr/bin/python3.5
# Renames a batch of files so that they are in a specific number order
# Author: Adrian Reid
# Date: 12/11/2013 (UK Format)

# IMPORTS
import argparse
import os

# ARGUMENT PARSER
parser = argparse.ArgumentParser()
parser.add_argument("extension", help = "The file extension of files we want to change. Can be '*' (include quotes)")
parser.add_argument("prefix", help = "The prefix for your new filenames")
args = parser.parse_args()

# Place arguments into easier to type variables
fileExt = args.extension
prefix = args.prefix

# GLOBAL VARIABLES
prevFiles = []
newFiles = []

# The function for changing the filename
def changeFileName(oldFile, count):
	# Create a new filename
	global prefix
	fileSplit = oldFile.split(".")
	fileExt = fileSplit.pop()
	prevFiles.append(oldFile)
	newFiles.append("%s%02d.%s" % (prefix, count, fileExt))
	#print (oldFile + "   --->   " + newFile)
	#os.rename(oldFile, newFile)

def renameFiles():
	global prevFiles, newFiles
	i = 0
	for curFile in prevFiles:
		print (curFile + "   --->   " + newFiles[i])
		i = i + 1
	response=input("Do you really want to rename all these files? Y or N: ")
	if response == "Y" or response == "y":
		i = 0
		for curFile in prevFiles:
			os.rename(curFile, newFiles[i])
			i = i + 1
	else:
		print ("No files renamed. Quitting...")
		exit()

# List all the files in the current directory then search for particular file extension
dirFiles = os.listdir()
dirFiles.sort()
counter = 1
for curFile in dirFiles:
	if fileExt == "*":
		changeFileName(curFile, counter)
		counter = counter + 1
	elif (curFile.endswith(fileExt)):
		changeFileName(curFile, counter)
		counter = counter + 1
renameFiles()
