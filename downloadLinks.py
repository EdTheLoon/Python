#!/usr/bin/python3.5
# Downloads links in the 'links' file. Updates the links file so that
# completed links are removed from the file and places completed links
# in a seperate file just in case they are needed again.

# IMPORTS
import os
import time
import argparse

# ARGUMENT PARSER
parser = argparse.ArgumentParser(
	description="A tool to download several HTTP links provided in a file.")
parser.add_argument(
	"-s",
	"--shutdown",
	help="Shut the system down after downloading has completed. (use sudo)",
	action="store_true")
parser.add_argument(
	"-f",
	"--file",
	help="-The links file to work with. Leave blank to use default (.links)",
	nargs="?",
	default=".links")
args = parser.parse_args()
linksList = args.file
shutAfter = args.shutdown


# GLOBAL VARIABLES
linksFile = ""
links = []
completedLinks = []

# READ THE LINKS FILE
def readLinks():
	global linksList
	linksFile = open(linksList, "r")
	for line in linksFile:
		links.append(line.rstrip("\n"))
	linksFile.close()

# UPDATE THE LINKS FILE
def writeLinks():
	global linksList
	linksFile = open(linksList, "w+")
	for link in links:
		linksFile.write("{}\n".format(link))
	linksFile.close()

# WRITE LINKS TO THE COMPLETED LINKS FILE
def writeComplete(curLink):
	completeFile = open(".complete", "a")
	completeFile.write("{}\n".format(curLink))
	completeFile.close()

# WRITE MESSAGES TO THE LOG FILE
def writeLog(logMsg):
	localTime = time.asctime(time.localtime(time.time()))
	msg = "[{}] {}\n".format(localTime, logMsg)
	logFile = open(".log", "a")
	logFile.write(msg)
	logFile.close()

# THE MAIN FUNCTION OF THE PROGRAM
def downloadLinks():
	readLinks()
	fileNum = 0
	for i in range(0, len(links)):
		writeLog("Starting link: {}".format(links[fileNum]))
		osres = os.system("aria2c --load-cookies=.cookie -x 5 -s 5 -k 50M -c {}".format(links[fileNum]))
#		osres = os.system("aria2c -x 5 -s 5 -k 20M -c --http-user=EMAILADDRESSHERE --http-passwd=PASSWORD {}".format(links[fileNum]))
		if osres == 0:
			writeLog("Completed link: {}".format(links[fileNum]))
			writeComplete(links[fileNum])
			links.pop(fileNum)
			writeLinks()
		else:
			writeLog("Error, returned {}".format(osres))
			writeLog("Error downloading {}".format(links[fileNum]))
			fileNum += 1

# Start the main function of the program
downloadLinks()

# Shutdown the system when complete
if shutAfter: 
	os.system("shutdown -h")
