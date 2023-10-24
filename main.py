import turtle
import tkinter


drawing_board = turtle.Screen()
drawing_board.bgcolor("pink")
drawing_board.title("Drawing shrinking square")
turtle_instance = turtle.Turtle()

def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5
shrinkingSquare(150)
shrinkingSquare(130)
shrinkingSquare(110)
shrinkingSquare(90)
shrinkingSquare(70)
shrinkingSquare(50)
shrinkingSquare(30)
shrinkingSquare(10)

turtle.done()
