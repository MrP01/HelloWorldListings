from turtle import *

def drawPolygon(length,edges):
	angle=360/edges
	for i in range(edges):
		forward(length)
		right(angle)

def drawRosette(size,parts,col):
	fillcolor(col)
	begin_fill()
	for i in range(parts):
		drawPolygon(size,parts)
		right(360/parts)
	end_fill()

if __name__ == "__main__":
	speed(0)
	color("green")
	for i in range(16):
		drawRosette(50,i+1,"orange")
		input(i+1)
		clear()
	input("Enter zum Beenden")
