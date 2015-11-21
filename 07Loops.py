from turtle import *

length=int(input("Laenge: "))
edges=int(input("Ecken: "))

angle=360/edges

for i in range(edges):
	print(i)
	forward(length)
	right(angle)

input("Enter zum Beenden")
