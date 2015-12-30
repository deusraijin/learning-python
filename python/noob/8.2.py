#!/usr/bin/env python

def gaycount(word,letter):
	count = 0

	for this_letter in word:
		if this_letter == letter:
			count+= 1
	return count

word = input('Enter your gay word:')
letter = input('Count this letter in your gay word:')

if (len(letter)!=1):
	print('fuck you')
else:
	print('Instances:'),
	print(gaycount(word,letter))
