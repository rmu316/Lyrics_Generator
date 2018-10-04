from fetch_data import *

def welcome():
	print "\nWelcome to the Lyrics Wizard!!!"
	print "Create new songs out of the old!\n"

def progress():
	print "Generating Markov Chain..."
	sleep(1)

def menu():
	print "\nSo here's how this works..."
	print "Enter the lyrics to songs you already know well. Then, our program will"
	print "generate a new song BASED off what you've inputed, which can be the next"
	print "BIG new hit song you wanted to write!\n"
	print "(1) Manually enter a song's lyrics into the console"
	print "(2) Load a local file containing the song's lyrics"
	print "(3) Load the song's lyrics from a website"
	print "(4) Exit this application"
	return raw_input("---> ")

def menu2():
	print "\nLyrics Wizard has processed your input!"
	print "Now you can view your results in several ways"
	print "(1) Show results on the console"
	print "(2) Write the results to a file"
	print "(3) Return to the main menu"
	print "(4) Exit the program"
	return raw_input("---> ")

welcome()

isRunning = True

while isRunning:
	try:
		option = int(menu())
	except ValueError:
		print "Invalid input given\n"
		continue
	output = []
	if option == 1:
		input = raw_input("Input song lyrics (containing at least 2 words) --> ")
		if validate(input, 1) == False:
			continue
		progress()
	elif option == 2:
		file_path = raw_input("What is the file path (relative to your current directory) of the lyrics?\nYour current directory is " + os.getcwd() + "\n --> ")
		progress()
		if validate(file_path, 2) == False:
			continue
		input = process_file(file_path)
	elif option == 3:
		url_path = raw_input("What is the URL path (e.g. http://<path to your file>) of the lyrics? --> ")
		progress()
		if validate(url_path, 3) == False:
			continue
		input = process_url(url_path)
	elif option == 4:
		isRunning = False
		print "Thanks for using the Lyrics Wizard!\n"
	else:
		print "Invalid input. Please try again\n"
	if option == 1 or option == 2 or option == 3:
		output = run_markov_chain(input)
		isRunning2 = True
		while isRunning2:
			try:
				option2 = int(menu2())
			except ValueError:
				print "Invalid input given"
				continue
			if option2 == 1:
				display_on_console(output)
			elif option2 == 2:
				write_to_file(output)
			elif option2 == 3:
				isRunning2 = False
			elif option2 == 4:
				isRunning2 = False
				isRunning = False
			else:
				print "Invalid input. Please try again\n"