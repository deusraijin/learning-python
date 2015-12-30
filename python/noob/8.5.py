#!/usr/bin/env python

def rotate_word(word, rotation):
	new_word = ''
	rot_letter = ''
	rot_by = overflow = 0

	for letter in word:
		rot_by = ord(letter) + int(rotation)
		if (rot_by < ord('a')):
			rot_by = ord('z') - (ord('a') - rot_by) + 1
		elif (rot_by > ord('z')):
			rot_by = ord('a') + (rot_by - ord('z')) - 1

		new_word += chr(rot_by)
	
	return new_word

oldword = input("Enter a gay sex phrase to rotate:")
rotby = input("Number of characters to rotate by:")

print("New word:"+rotate_word(oldword, rotby))
