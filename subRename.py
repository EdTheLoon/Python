#!/usr/bin/python3.5
######################### Subtitle Rename ##############################
# Take two files and rename the subtitle file to match the video file
# Author: Adrian Reid
# Date: 26/12/2016
########################################################################

### IMPORTS ############################################################
import os
import argparse

### ARG PARSER #########################################################
parser = argparse.ArgumentParser()
parser.add_argument(
	"video",
	help="The video file to match the filename to")
parser.add_argument(
	"sub",
	help="The subtitle file to rename")
args = parser.parse_args()

videoFile = args.video
subFile = args.sub

### MAIN PROGRAM #######################################################
vidSplit = videoFile.split(".")
subSplit = subFile.split(".")
subExt = subSplit.pop()
newSub = ""

# Get rid of file extension in video filename
vidSplit.pop()

# Iterate through vidSplit to create new subtitle filename
for split in vidSplit:
	newSub += split + "."

# Add the subtitle extension
newSub += subExt

# Rename the subtitle file
osres = os.system("mv {} {}".format(subFile, newSub))
