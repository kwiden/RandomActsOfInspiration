import random

#import phrases
with open("file.txt") as file:
	phrases = []

#import nouns

#generate quote
def new_quote():
	return "quote"

print("Press enter for new phrase, q for quit")
while True:
	val = input("")
	if val == "q":
		break
	print(new_quote())


#hints:
# random.randomint(low,high)
# .readlines()
# .append(object)
# .rstrip()
# while "" in ""
