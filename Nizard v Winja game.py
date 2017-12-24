import random, time
"""setup global variables here"""
headings= ["speed", "strength", "skill", "magic", "intelligence", "stamina"] #dermines names and number of attibutes
wizard=[]# holds attribute values
ninja =[]

fileName ="" #empty string to hold name of current file for results

wizardScore = 0 #records how many  atrributes wizard wins
ninjaScore = 0 #records how many  atrributes ninja wins


def diceAdd(num1):
#accepts the attribute value as the parameter
#rolls a dice and adds the number passed in to it
	diceroll = random.randint(2,12)
	total = num1+diceroll
	print("You rolled ",diceroll, " your total score is ", total)
	return total # returns sum of parameter and diceroll
# end of dice add  function

def updateFile(wizard, ninja, attribute, winner):
	global fileName
	ninja = str(ninja)
	wizard = str(wizard)
	"""Procedure to write outcomes from compare() to file
	file must be created first""" 
	if fileName != "":
		fo = open(fileName,"a") 
		fo.write(attribute+"\t"+wizard+"\t"+ninja+"\t"+winner+"\n")
		fo.close()
	else:
		print("something went wrong with file write operation")
	return #end of procedure

def compare(wizard, ninja, attribute):
	# how many arguments are set for this function>>>
	#compare the wizard and ninja score for each attribute
	global wizardScore, ninjaScore # allows us to change these variables outside the function
	winner = ""
	if wizard == ninja:
		#what happens here????
		winner = "draw"
		print(attribute, "was a draw")
	elif wizard > ninja:
		#wizard beats ninja
		print("Wizard beat Ninja for ", attribute)
		#what happens here????
		winner = "wizard"
		wizardScore = wizardScore +1
	else:
		print("Ninja beat Wizard for ", attribute)
		#what happens here????
		winner = "ninja"
		ninjaScore = ninjaScore + 1
		time.sleep(2)
	print("please wait while the results are written to a file")
	updateFile(wizard, ninja, attribute ,winner)
	return # this function returns nothing
	#end of compare function

def setupAttrib(player, playerList, headings): 
	# holds name of player and which list to add to
	inputVal = None
	for i in range(0, len(headings)):
		print(player, "what is you modifier for", headings[i], "?")
		while True:
			inputVal =input("Enter here: ")
			if inputVal.isdigit() == True:
				inputVal = int(inputVal)
				if inputVal >= 0 and inputVal <11:
					break
				else:
					print("no cheating!")
			else:
				print("not a valid entry")
		inputVal = diceAdd(inputVal)
		playerList.append(inputVal)
	return
def createFile():
	global fileName
	"""Procedure to create a new file for the game """
	nowTime = time.strftime("%H:%M:%S")
	fileName = "NizzardWinja" + nowTime + ".txt"
	fo = open(fileName,"wt")
	fo.write("---------------------------------------")
	fo.write("\n")
	fo.write("Attribute"+"\t"+"Wizard Score"+"\t"+"Ninja Score"+"\t"+"winner"+"\n")
	fo.write("\n")
	fo.close()
	return #end of procedure
""" end of functions section """

print("""Welcome to Wizard v Ninja
Wizard enter your attribute values""")
setupAttrib("wizard", wizard, headings)
print("""Wizard Complete
Ninja enter your attribute values""")
setupAttrib("ninja", ninja, headings)
print("Rolling complete")
createFile() #set up file to save results

while wizardScore < 3 and ninjaScore < 3:
	#print game menu
	print("Option \t Heading")
	for i in range(0, len(headings)):
		print(i, "\t", headings[i])

	print("""Wizard, enter the Option No of the attribute to play""")
	toPlay = int(input("Enter the option number to play"))
	if toPlay >= 0 and toPlay < len(headings):
		print("You chose ", headings[toPlay])
		compare(wizard[toPlay], ninja[toPlay], headings[toPlay] )
	else:
		print("Sorry that is not an option")
	time.sleep(2)

if wizardScore > ninjaScore:
	print ("Wizard is the victor - the Ninja is destroyed by his mighty magic")
else:
	print ("Ninja is the victor - the wizard is sliced in half by his blade")

