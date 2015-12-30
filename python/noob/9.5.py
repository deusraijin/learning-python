#!/usr/bin/env python

fin = open('words.txt')

def avoids(word, letters):
	for letter in letters:
		if letter in word:
			return False
	return True

def uses_only(word, letters):
	for character in word:
		if character not in letters:
			return False
	return True

def uses_all(word, letters):
	for letter in letters:
		if letter not in word:
			return False
	return True

def is_abecedarian(word):
	i = 1
	while i < len(word):
		if ord(word[i]) < ord(word[i-1]):
			return False
		i += 1
	return True

def perc(num1, num2):
	return (num1*1.0 / num2 * 100)

line_count = 0
line_count_noe = 0
line_count_abec = 0

for line in fin:
	word = line.strip()
	line_count += 1

	if (avoids(word, 'e')):
		line_count_noe += 1

	if (is_abecedarian(word)):
		line_count_abec += 1

print("Abecedarian words: "),; print(perc(line_count_abec, line_count))
print("Doesn't use e:"),; print(perc(line_count_noe, line_count)) 


		
