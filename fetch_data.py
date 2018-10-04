from markov_python.cc_markov import MarkovChain
from time import sleep
from datetime import datetime
import os
import urllib2

WORD_BREAK = 10

def validate(input, type):
	isGood = True
	if type == 1:
		if len(input.split()) < 3:
			print "Not enough words to create inspiration! Try again\n"
			isGood = False
	if type == 2:
		try:
			open(input, "r")
		except:
			print "File open failed. Check again if the file exists at that path\n"
			isGood = False
	if type == 3:
		try:
			urllib2.urlopen(input)
		except:
			print "URL link given not accessible. Open a browser and see if you can open that URL\n"
			isGood = False
	return isGood

def process_file(file_path):
	file = open(file_path, "r")
	output = file.read()
	file.close()
	return output

def process_url(url_path):
	response = urllib2.urlopen(url_path)
	return response.read()

def display_on_console(output):
	print "\nHere's " + str(len(output)) + " significant words we found in your lyrics:"
	for word in output:
		print word,
	print "\n\n"

def write_to_file(output):
	filename = "lyrics_on_"+str(datetime.now())
	file = open(filename, "w")
	wrdCnt = 0;
	for word in output:
		if wrdCnt % WORD_BREAK == 0:
			file.write("\n")
		file.write(word + " ")
		wrdCnt += 1
	print "Done. You can see the output at " + filename + "\n\n"

generateText = MarkovChain()

def run_markov_chain(input):
	generateText.add_string(input)
	return generateText.generate_text(len(input))