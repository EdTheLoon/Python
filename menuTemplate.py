#!/usr/bin/python3.5
# A TEMPLATE FOR CREATING A MENU

# IMPORTS
import os

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
		print ("""1. Option 1
2. Option 2
3. Option 3
4. Option 4
5. Option 6
7. Option 7
8. Option 8
9. Option 9
0. Exit""")
		try:
			menuR = eval(input("Please select an option: "))
		except Exception:
			print("Invalid selection. Please try again".format(menuR))
		else:
			if menuR == 1:
				print ("Chose 1")
			elif menuR == 2:
				print ("Chose 2")
			elif menuR == 3:
				print("Chose 3")
			elif menuR == 4:
				print("Chose 4")
			elif menuR == 5:
				print("Chose 5")
			elif menuR == 6:
				print("Chose 6")
			elif menuR == 7:
				print("Chose 7")
			elif menuR == 8:
				print("Chose 8")
			elif menuR == 9:
				print("Chose 9")
			elif menuR == 0:
				print("Chose 0")
		input("Press enter to continue...")
### END OF MENU BLOCK ##################################################

# Call the menu
menuPrompt()
