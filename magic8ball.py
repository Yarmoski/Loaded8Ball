#THE LOADED MAGIC 8 BALL


#INSTRUCTIONS:

#Input a "space" character BEFORE your question to guarantee that the ball returns a "yes" variant answer
#Input a "space" character AFTER your question to guarantee that the ball returns a "no" variant answer
#Do not put a space before or after for an authentic magic 8-ball with all 20 answers including "maybe" variants


import random
import sys
import time

answers_list = [
	"\nIt is certain.",
	"\nIt is decidedly so.",
	"\nWithout a doubt.",
	"\nYes - definitely.",
	"\nYou may rely on it.", 
	"\nAs I see it, yes.",
	"\nMost likely.", 
	"\nOutlook good.", 
	"\nYes.", 
	"\nSigns point to yes.", 
	"\nReply hazy, try again.",
	"\nAsk again later.", 
	"\nBetter not tell you now.", 
	"\nCannot predict now.", 
	"\nConcentrate and ask again.", 
	"\nDon't count on it.",
	"\nMy reply is no.", 
	"\nMy sources say no.",
	"\nOutlook not so good.",
	"\nVery doubtful."
	]

answers_list_positive = [
	"\nIt is certain.",
	"\nIt is decidedly so.",
	"\nWithout a doubt.",
	"\nYes - definitely.",
	"\nYou may rely on it.", 
	"\nAs I see it, yes.",
	"\nMost likely.", 
	"\nOutlook good.", 
	"\nYes.", 
	"\nSigns point to yes.",
	]

answers_list_negative = [
	"\nDon't count on it.",
	"\nMy reply is no.", 
	"\nMy sources say no.",
	"\nOutlook not so good.",
	"\nVery doubtful."
	]

def scrolling_text(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.03)

def scrolling_text_slow(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.3)

while True:
	#First thing the user sees
	intro = "\nAsk me anything...as long as it is a yes or no question."
	scrolling_text(intro)
	player_input = input("\n")


	#displays the answer if user inputs something
	if player_input == "":
		exit_string = "\nYou have chosen to leave... (Press Enter)"
		scrolling_text(exit_string)
		input("")
		break
	#user puts a space before question to guarantee "yes" answer
	elif player_input[0] == " ":
		#"Thinking"
		hmm = "\nHmm..."
		scrolling_text_slow(hmm)
		time.sleep(1)

		#selects a random choice from the positive list
		answer = random.choice(answers_list_positive)

		#displays answer and reprompts
		scrolling_text(answer)
		again_string = "\n\n\nWould you like to ask another question?"
		scrolling_text(again_string)
		choice = input("\n")
		if choice.lower() in ["yes", "ya", "ye", "sure", "ok", "yeah", "y"]:
			knew_string = "\nI knew you would."
			scrolling_text(knew_string)
			pass
		else:
			bye_string = "\nI knew you wouldn't. (Press enter)"
			scrolling_text(bye_string)
			input("")
			break

	#user puts a space after question to guarantee "no" answer
	elif player_input[-1] == " ":
		#"Thinking"
		hmm = "\nHmm..."
		scrolling_text_slow(hmm)
		time.sleep(1)

		#selects a random choice from the negative list
		answer = random.choice(answers_list_negative)

		#displays answer and reprompts 
		scrolling_text(answer)
		again_string = "\n\n\nWould you like to ask another question?"
		scrolling_text(again_string)
		choice = input("\n")
		if choice.lower() in ["yes", "ya", "ye", "sure", "ok", "yeah", "y"]:
			knew_string = "\nI knew you would."
			scrolling_text(knew_string)
			pass
		else:
			bye_string = "\nI knew you wouldn't. (Press enter)"
			scrolling_text(bye_string)
			input("")
			break


	#user is unaware that the app can be controlled
	else:
		#"Thinking"
		hmm = "\nHmm..."
		scrolling_text_slow(hmm)
		time.sleep(1)

		#selects a random choice from all possible answers
		answer = random.choice(answers_list)

		#displays answer and reprompts
		scrolling_text(answer)
		again_string = "\n\n\nWould you like to ask another question?"
		scrolling_text(again_string)
		choice = input("\n")
		if choice.lower() in ["yes", "ya", "ye", "sure", "ok", "yeah", "y", " yes"]:
			knew_string = "\nI knew you would."
			scrolling_text(knew_string)
			pass
		else:
			bye_string = "\nI knew you wouldn't. (Press enter)"
			scrolling_text(bye_string)
			input("")
			break
		

