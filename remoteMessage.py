#!/usr/bin/python3.5
# A TEMPLATE FOR CREATING A MENU

# IMPORTS
import os

# Set display to 0
os.system("export DISPLAY=:0")

def wait():
	input("Press enter to continue...")

def getIcon():
	#print("Icon types: info, question, warning and error")
	#_icon = input("Icon:    ")
	try:
		cls()
		print("""1. Information
2. Question
3. Warning
4. Error""")
		option = eval(input("Choose an icon: "))
	except Exception:
		input("Invalid input. Please try again. Press enter to continue...")
	else:
		if option == 1:
			_icon = "info"
		elif option == 2:
			_icon = "question"
		elif option == 3:
			_icon = "warning"
		else:
			_icon = "error"
	cls()
	print("Icon:    {}".format(_icon))
	return _icon
	
def getText():
	_text= input("Message: ")
	return _text
	
def getTimeout():
	_timeout = input("Timeout: ")
	return _timeout

def getTitle():
	_title = input("Title:   ")
	return _title
	
def zenity(msg):
	print(msg)
	wait()

def notification():
	icon = getIcon()
	text = getText()
	os.system("zenity --notification --window-icon=\"{}\" --text=\"{}\""
		.format(icon, text))
	
def info():
	icon = getIcon()
	title = getTitle()
	text = getText()
	os.system("zenity --{} --title=\"{}\" --text=\"{}\""
		.format(icon, title,  text))

def yesNo():
	title = getTitle()
	text = getText()
	res = os.system("zenity --question --title=\"{}\" --text=\"{}\""
		.format(title, text))
	if res == 256:
		zenity("They replied, 'no'")
	else:
		zenity("They replied, 'yes'")
	
def question():
	title = getTitle()
	text = getText()
	res = os.popen("zenity --entry --title=\"{}\" --text=\"{}\""
		.format(title, text), "r")
	reply = res.read()
	zenity("They replied: {}".format(reply))
	
def calQuestion():
	title = getTitle()
	text = getText()
	res = os.popen("zenity --calendar --title=\"{}\" --text=\"{}\""
		.format(title, text), "r")
	reply = res.read()
	zenity("They replied: {}".format(reply))

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
		print ("""1. Notification
2. Info Message
3. Yes/No Question
4. Question with text reply
5. Calendar Question
0. Quit""")
		try:
			menuR = eval(input("What do you want to send: "))
		except Exception:
			print("Invalid selection. Please try again")
			wait()
		else:
			if menuR == 1:
				cls()
				notification()
			elif menuR == 2:
				cls()
				info()
			elif menuR == 3:
				cls()
				yesNo()
			elif menuR == 4:
				cls()
				question()
			elif menuR == 5:
				cls()
				calQuestion()
			elif menuR == 6:
				print("Chose 6")
			elif menuR == 7:
				print("Chose 7")
			elif menuR == 8:
				print("Chose 8")
			elif menuR == 9:
				print("Chose 9")
			elif menuR == 0:
				print("Quitting...")
### END OF MENU BLOCK ##################################################

# Call the menu
menuPrompt()
