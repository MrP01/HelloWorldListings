from turtle import *

def _forward():
	forward(50)
def _backward():
	backward(50)
def _right():
	right(30)
def _left():
	left(30)

if __name__ == "__main__":
	showturtle()
	onkey(_forward,"Up")
	onkey(_backward,"Down")
	onkey(_right,"Right")
	onkey(_left,"Left")
	onkey(undo,"u")
	listen()

	input("Enter zum Beenden")
