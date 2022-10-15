# ******TO DOs IN PROGRAM (OPTIONAL)*****
#Show high score in all attempts
#Display all the scores

# ****CURRENT FUNCTIONALITIES****
# Show questions in random order everytime
# If user press Enter the question is skipped
# Doesn't let user input any invalid option, doesn't let user leave question or option input while adding questions
# Show percentage of user

#Just a line to test github push

# checking push after cloning git repo

import random

#FUNCTION TO ADD A QUESTION
def add_ques(subj): #Take subject as argument
	"""Input : Takes subject as input
	   Output : Add given question to the respective subject question bank file"""

	if subj.upper() == "SCI":
		f_sci = open("Science Question Bank List Version.txt","a+") #Open file in append+ mode
		while True:
			ques = input("Enter the question: ") #Input the quesion
			if ques == "": # "" means user pressed Enter
				print()
				print("Please enter a question") #If user enters empty string then ask again for a valid question
				print()
			else:
				break #If input is not an empty string then break out of loop
		while True:
			opt_a = input("Enter option a: ") #Input the option a
			if opt_a == "": # "" means user pressed Enter
				print()
				print("Please enter a valid option")  #If user enters empty string then ask again for a valid option
				print()
			else:
				break
		while True:
			opt_b = input("Enter option b: ") #Input the option a
			if opt_b == "":
				print()
				print("Please enter a valid option")
				print()
			else:
				break
		while True:
			opt_c = input("Enter option c: ") #Input the option a
			if opt_c == "":
				print()
				print("Please enter a valid option")
				print()
			else:
				break
		while True:
			opt_d = input("Enter option d: ") #Input the option a
			if opt_d == "":
				print()
				print("Please enter a valid option")
				print()
			else:
				break

		while True:
			opt = input("Enter the correct option (a/b/c/d):  ") #Input the correct asnwer
			opt = opt.lower()
			if opt != "a" and opt != "b" and opt != "c" and opt != "d": # If user anything other than a,b,c or d,
				print()
				print("Please enter an option between a,b,c and d")#  then ask again for a valid option
				print()
			else:
				break # If user enters a valid option then break out of loop
		ques_write = "\n\n" + ques +"\n" + "a. " + opt_a + "\n" + "b. " + opt_b + "\n" + "c. " + opt_c + "\n" + "d. " + opt_d + "\n" +opt
		f_sci.write(ques_write) # Write in the file in the above format
		print()
		print("Question has been added")
		f_sci.close() #Close file

	elif subj.upper() == "PST": # Same code for PST
		f_pst = open("PST Question Bank List Version.txt", "a+")
		while True:
			ques = input("Enter the question: ")
			if ques == "":
				print()
				print("Please enter a question")        #SAME CODE FOR A DIFFERENT SUBJECT
				print()
			else:
				break
		while True:
			opt_a = input("Enter option a: ")
			if opt_a == "":
				print()
				print("Please enter a valid option")
				print()
			else:
				break
		while True:
			opt_b = input("Enter option b: ")
			if opt_b == "":
				print()
				print("Please enter a valid option")
				print()
			else:
				break
		while True:
			opt_c = input("Enter option c: ")
			if opt_c == "":
				print()
				print("Please enter a valid option")
				print()
			else:
				break
		while True:
			opt_d = input("Enter option d: ")
			if opt_d == "":
				print()
				print("Please enter a valid option")
				print()
			else:
				break

		while True:
			opt = input("Enter the correct option (a/b/c/d):  ")
			opt = opt.lower()
			if opt != "a" and opt != "b" and opt != "c" and opt != "d":
				print()
				print("Please enter an option between a,b,c and d")
				print()
			else:
				break
		ques_write = "\n\n" + ques +"\n" + "a. " + opt_a + "\n" + "b. " + opt_b + "\n" + "c. " + opt_c + "\n" + "d. " + opt_d +"\n"+opt
		f_pst.write(ques_write)
		print("Question has been added")
		f_pst.close()


#FUNCTION TO VIEW ALL QUESTIONS OF A SUBJECT
def quiz_view(subj): #Take subject as argument
	if subj.upper() == "SCI":
		with open("Science Question Bank List Version.txt") as f_sci:
			print()
			print("*****QUESTIONS OF SCIENCE QUIZ*****")
			print()
			print("-------Correct option is displayed in the last of each question-------")
			print(f_sci.read()) # Print the whole question bank file as it is
	if subj.upper() == "PST":
		with open("PST Question Bank List Version.txt")as f_pst:
			print()
			print("*****QUESTIONS OF PST QUIZ*****")
			print()
			print("-------Correct option is displayed in the last of each question-------")
			print(f_pst.read()) # Print the whole question bank file as it is
	while True:
		print()
		cho_ice = input("Do you want to add any question? (Y/N): ") # Prompt to add any question
		cho_ice = cho_ice.upper()
		if cho_ice != "Y" and cho_ice != "N": # Re-ask if other than Y or N is entered
			print()
			print("Please choose between Y and N")
			print()
		else:
			break # If a valid option is entered then break out of loop
	if cho_ice == "Y":
		while True:
			print()
			add_ques(subj) # If choice is Y then add a question of subject for which view funcion is called
			while True:
				print()
				v_choice = input("Do you want to add another question? (Y/N): ")#After adding one question,ask for another
				v_choice = v_choice.upper()
				if v_choice != "Y" and v_choice != "N":
					print()
					print("Please choose between Y and N")
					print()
				else:
					break
			if v_choice == "Y": # If answer is positive then,
				add_ques(subj) # again add question of subject for which view function is called
			else:
				return v_choice # If answer is negative then return the answer
				break # break out of loop
	else: # If first choice is negative then,
		return cho_ice # return the first choice





def manage():
	while True:
		m_choice = input("Select Your Option: \n1. View Questions\n2. Add Question\n")
		m_choice = m_choice.upper()
		if m_choice != "1" and m_choice != "2": #If input is not V neither A then,
			print("Please select b/w 1 and 2: ") # re-ask for a valid option
		else:
			break # If input is valid then, break out of loop
	if m_choice == "1":
		while True:
			sub = input("Enter the subject (PST/SCI): ") # If input is V then ask the subject to be viewd
			sub = sub.upper()
			if sub != "PST" and sub != "SCI": #If input is not PST neither A then,
				print()
				print("Please choose between PST and SCI")# re-ask for a valid option
				print()
			else:
				break
		return quiz_view(sub) # Return the first choice of view function

	else:
		while True:
			while True:
				subjt = input("Enter the subject (PST/SCI): ")
				subjt = subjt.upper()
				if subjt != "PST" and subjt != "SCI":
					print()
					print("Please choose between PST  and SCI")
					print()
				else:
					break
			add_ques(subjt)
			while True:
				add_choice = input("Do you want to add another question? (Y/N): ")
				add_choice = add_choice.upper()
				if add_choice != "Y" and add_choice != "N":
					print()
					print("Please choose between Y and N")
					print()
				else:
					break
			if add_choice == "Y":
				add_ques(subjt)
			else:
				break
	return add_choice


#FUNCTION TO LOGIN IN APP AND PROMPT IF THE USER WANTS TO MANAGE OR TAKE THE QUIZ
def login():
	while True:
		user_name = input("Enter your username: ")
		if user_name == "":
			print()
			print("This field is mandatory!")
			print()
		else:
			break
	while True:
		pwd = input("Enter your password: ")
		if pwd == "":
			print()
			print("This field is mandatory!")
			print()
		else:
			break
	print()
	print("WELCOME TO QUIZ APP - "+ "'" +user_name + "'")
	print()
	while True:
		choice = input("Select Your Option: \n1. Take Quiz\n2. Manage Quiz\n")
		choice = choice.upper()
		if choice != "1" and choice != "2":
			print("Please choose between T and M")
			print()
		else:
			break
	return choice


def quiz():
	while True:  # Run in loop untill user responds No to restart() function

		while True:  # Ask user to enter a valid option untill he/she does so
			subj = input("Choose the subject (PST or Sci): ")
			subj = subj.upper()

			if subj != "PST" and subj != "SCI":
				print()
				print("Please choose between PST or Sci")
				print()
			else:
				break  # Get out of loop if user enters a valid option for subj

		if subj == "PST":
			pst_quiz()  # If user enter PST call function to take PST Quiz
			if not restart():  # When quiz is done ask to restart or not
				break  # If restart() is False break out of 'While True' loop and print the end message other wise continue

		elif subj == "SCI":
			sci_quiz()  # If user enter PST call function to take SCIENCE Quiz
			if not restart():  # When quiz is done ask to restart or not
				break  # If restart() is False break out of 'While True' loop and print the end message other wise continue
	print("THANKS FOR PLAYING!")  # In the end display end message
	print()


# FUNCTION TO RETURN LIST OF QUESTIONS(LIST OF DICTIONARIES),
def fetch_ques(ques_bank):
	"""Input : takes input the handler of file
	   Return : List of questions (a 2-D List)"""

	global ques_lst
	q = ques_bank.read()
	ques_lst = []  # Initialize List of Questions
	lst_q = q.split("\n\n")  # Separating questions by gap(double enter)
	for i in lst_q:
		ques_lst.append(i.split("\n"))
	return ques_lst




# FUNCTION TO ASK THE QUESTIONS AND STORE THE USER'S INPUT AND RETURN True or False BASED ON USER'S ANSWER
def ask_ques(num):
	q_num = num +1
	while True:
		print()
		print("Q"+str(q_num)+": "+ques_lst[num][0]+"\n"+ques_lst[num][1]+"\n"+ques_lst[num][2]+"\n"+ques_lst[num][3]+"\n"+ques_lst[num][4])  # Generating Q.No. before comma and printing question after comma by accessing it through list of questions and "Q.No." key value
		ans = input("Choose the correct answer: ")  # Take answer as input from user
		ans = ans.lower()
		if ans != "a" and ans != "b" and ans != "c" and ans != "d" and ans != "":  # If user press Enter an empty string will be stored in ans
			print()  # To leave an empty line
			print("Please choose a valid option (a/b/c/d). Or press 'Enter' to skip the question")
		# Repeatedly ask the question untill user enters a valid option
		elif ans == "":  # Empty string is a valid option, it means user pressed Enter.
			print()
			print("This question is skipped")  # Question will be skipped
			break  # Get of while loop if the ans is a valid option
		else:
			break  # Get of while loop if the ans is a valid option
	return ans == ques_lst[num][5]  # return True if answer is correct, otherwise return False
												# Here Empty string(Enter Key) will also return False, hence in both conditions score will not increment


# FUNCTION TO RUN THE QUIZ AND DISPLAY SCORE
def quiz_run():
	random.shuffle(ques_lst) #Shuffle list randomly everytime
	score = 0 #Initialize Score
	for i in range(10):  # Displaying questions sequencially
		print()  # To leave an empty line
		if ask_ques(i): # If ask_ques() returns True, score is increment
			score += 1
	percent = round((score / len(ques_lst) * 100), 2)
	print()
	print("Your score is", score, "out of", len(ques_lst))
	print("You got", str(percent) + "%")
	if percent >= 30:
		print("Congratulations! You passed the quiz")
	else:
		print("You failed. Better luck next time!")
	print()


# FUNTION TO ACTUALLY TAKE THE QUIZ, IT WILL TAKE QUESTION BANK'S FILE HANDLER AS ARGUMENT AND TAKE THE WHOLE QUIZ
def take_quiz(ques_bank):
	fetch_ques(ques_bank)
	quiz_run()

#FUNCTION TO RESTART THE QUIZ
def restart():
	"""Input : Ask user to restart quiz or not
	   Return : returns whether user's response is Yes (Y) or not"""

	while True:
		cont = input("Do you want to replay? (Y/N): ")
		print()
		cont = cont.upper()
		if cont != "Y" and cont != "N":
			print()
			print("Please choose a valid option (Y/N): ")
			continue
		else:
			break
	return cont.upper() == "Y" # Returns True if user enters Y, False otherwise

# FUNCTION TO TAKE PST QUIZ
def pst_quiz():
	f_pst = open("PST Question Bank List Version.txt")
	take_quiz(f_pst)
	f_pst.close()

# FUNCTION TO TAKE SCIENCE QUIZ
def sci_quiz():
	f_sci = open("Science Question Bank List Version.txt")
	take_quiz(f_sci)
	f_sci.close()

# ****ACTUAL PROGRAM****
while True:
	print()
	print('''===========================================
--------------- QUIZ GAME ---------------
===========================================''')
	if login() == "1":
		if not quiz():
			while True:
				ch = input("Do you want to quit the app? (Y/N): ")
				ch = ch.upper()
				if ch != "Y" and ch != "N":
					print()
					print("Please choose between Y and N")
					print()
				else:
					break
			if ch == "N":
				continue
			else:
				break

	else:
		if manage() == "N":
			while True:
				print()
				ch = input("Do you want to quit the app? (Y/N): ")
				ch = ch.upper()
				if ch != "Y" and ch != "N":
					print()
					print("Please choose between Y and N")
					print()
				else:
					break
			if ch == "N":
				continue
			else:
				break


