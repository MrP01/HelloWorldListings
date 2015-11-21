from turtle import *

def drawYin(size,col):
	fillcolor(col)
	begin_fill()
	circle(size,180)
	circle(2*size,180)
	rt(180)
	circle(-size,180)
	end_fill()

def drawYinYang(size,col1,col2):
	drawYin(size,col1)
	rt(180)
	drawYin(size,col2)

if __name__ == "__main__":
	drawYinYang(50,"green","blue")
	input("Enter zum Beenden")
