# Madlib project


placeHolders = ['___1___','___2___','___3___','___4___']

rules = "You will get 5 guesses per problem, Good Luck\n"

answers = {'python' : ['world','python','print','html'],
		   'harry potter' : ['harry','hogwarts','hermione','ron'],
           'star wars' : ['force','jedi','sith','han']}           

text = { 
'python' : '''A common first thing to do in a language is display
'Hello ___1___!'  In ___2___ this is particularly easy; all you have to do
is type in:
__3__ "Hello ___1___!"
Of course, that isn't a very useful thing to do. However, it is an
example of how to output to the user using the ___3___ command, and
produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an ___4___ file in a browser, but it's
a step in learning ___2___ syntax, and that's really its purpose.''',

'harry potter' : '''___1___ potter is a magical story about a magic users and muggels. it 
starts off with ___1___ being excepted to ___2___ school of witchcraft and wizardy. 
___1___'s best friends are ___3___ granger and ___4___ weasley.  
''',

'star wars' : '''Star Wars is a serious that united the generations. The series is based 
around the use of the ___1___. There are ___2___ and ___3___ who are trained in the are of the
force. ___2___ in the light and ___3___ in the dark. oh yeah, dont forget about ___4___ solo and chewbacca'''}


def chooseLevel():
	#prompts the user to select which trivia
	#return the apropriate text and answers
	user_choice = ""
	rightAnswers = ['python','harry potter','star wars']
	while user_choice not in rightAnswers:
		user_choice = raw_input("what level do you want to play: Python | Harry Potter | Star Wars\n").lower()
	print 'You chose '+user_choice+"!!!\n"	 
	return text[user_choice],answers[user_choice]

def checkAnswer(rightAnswer,placeHolder):
	# checks to see if the guess matches the answer
	# sets the guess limit to 5 per answer
	# returns guess if true
	count = 0
	user_choice =" "
	while user_choice != rightAnswer:
		count += 1
		user_choice = raw_input("\nWhats the answer for "+placeHolder+"? ").lower()
		if count == 5: 
			print '\nThat was your 5th fail. Game Over\n'
			exit()
	print "\nCorrect!!!!!!\n"		 
	return user_choice	

def letsPlay():
	index = 0
	text,answers = chooseLevel()
	print rules
	while index < len(placeHolders):
		print 'The current paragraph reads:'
		print text
		replaced = []
		text = text.split(" ")
		rightAnswer = answers[index]
		user_choice = checkAnswer(rightAnswer,placeHolders[index])
		for word in text:
			if placeHolders[index] in word:
				word = word.replace(placeHolders[index],user_choice)
			replaced.append(word)
		text = " ".join(replaced)
		index +=1
	print text	
	print '\nCongrats on winning!!!\n'		

letsPlay()			








