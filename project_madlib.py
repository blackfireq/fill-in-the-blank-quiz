# Madlib project
# Ask the user for the level of difficulty
# some extra notes


placeHolders = ['___1___','___2___','___3___','___4___']
anwsers = [['function','quotes','nothing','list'],
		   ['function','quotes','nothing','list'],
           ['function','quotes','nothing','list']]

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''


#check if word is one on the keywords


# ask for answers for each answer one at a time then fill in the paragraph
## get user input
## go through string to find all instantances of the current answer
## wash and repeat 

def chooseLevel():
	user_choice = ""
	rightAnswers = ['easy','medium','hard']
	while user_choice not in rightAnswers:
		user_choice = raw_input("what level do you want to play: Easy | Medium | Hard\n").lower() 
	return user_choice

def letsPlay(text,difficulty_level):
	index = 0
	print text
	while index < len(placeHolders):
		replaced = []
		text = text.split(" ")
		rightAnswers = anwsers[0] # need to fix later
		user_choice = checkAnswer(rightAnswers[index])
		for word in text:
			if placeHolders[index] in word:
				word = word.replace(placeHolders[index],user_choice)
			replaced.append(word)
		text = " ".join(replaced)
		print text
		index +=1	
	
def checkAnswer(rightAnswer):
	count = 0
	user_choice =" "
	while user_choice not in rightAnswer:
		count += 1
		user_choice = raw_input("Whats the answer?\n").lower()
		if count == 5: 
			print 'Game Over'
			exit() 
	return user_choice	

letsPlay(sample,chooseLevel())			








