#!/usr/bin/env python

def is_palindrome(word):
	return word == word[::-1]

word = input("Enter your gay word: ")

if is_palindrome(word):
	print("it's reversed man! whoaoa")
else:
	print("nope")
