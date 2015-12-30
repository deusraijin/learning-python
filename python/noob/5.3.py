#!/usr/bin/env python

def is_triangle(a,b,c):
	if a+b<c or a+c<b or b+c<a:
		print("Your triangle sucks")
	else:
		print("Your triangle is OK")

print("Input the a,b,c legs of a triangle to see if that's kosher")
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
is_triangle(a,b,c)
