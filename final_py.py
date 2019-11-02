# Skeleton Code at https://github.com/kwiden/RandomActsOfInspiration
import random

#import phrases
with open("phrases.txt") as file:
	phrases = []
	lines = file.readlines()

	for line in lines:
		phrases.append(line)

#import nouns
with open("nouns.txt") as file:
	nouns = []
	lines = file.readlines()

	for line in lines:
		line = line.rstrip()
		nouns.append(line)

#generate quote
def new_quote():
	#[PHRASE 1][PHRASE 2][]
	this_phrase = random.randint(0, len(phrases)-1)
#	this_noun = random.randint(0, len(nouns)-1)
	phrase = phrases[this_phrase]
	while "_" in phrase:
		this_noun = random.randint(0, len(nouns)-1)
		phrase = phrase.replace("_", nouns[this_noun], 1)

	return phrase

print("Press enter for new phrase, q for quit")
while True:
	val = input("")
	if val == "q":
		break
	print(new_quote())


#hints:
# random.randint(low,high)
# .readlines()
# .append(object)
# .rstrip()
# while "" in ""
