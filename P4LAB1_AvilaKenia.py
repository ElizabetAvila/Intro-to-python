
# Kenia Avila
#11/7/2024
#P4LAB1
#Draw a square and triangle using turtle library
#while loop to draw a square
import turtle
win = turtle.Screen()
t = turtle.Turtle()
win.bgcolor("black")
t.pensize(10)
t.pencolor("pink")
t.shape("arrow")
num = 0
while num<4:
 
t.forward(150)
 
t.right(90)
 
num += 1
print("while loop ends")
#while loop to draw a triangle
for tr in range(0,3):
 
t.left(120)
 
t.forward(200)
print("for loop has ended")
