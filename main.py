#Task4
def startriangle(n):
    if n > 0:
        print("*" * n)
        startriangle(n - 1)

startriangle(6)

#Task5
def triangular(n):
    if n == 1:
        return 1
    else:
        return n + triangular(n - 1)

print(triangular(7))

#Task6
def fibonacci(n):
    a, b = 1, 1
    for i in range(n -1):
        a, b = b, a + b
    print(a)
fibonacci(12)

#Task7 

#Task 8

#Task 9
import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.color("green")
pen.speed(0)
pen.left(90)

def fractaltree(n, length, angle, scale):
    if n == 0:
        return

    pen.forward(length)

    pen.left(angle)
    fractaltree(n - 1, length * scale, angle, scale)

    pen.right(2 * angle)
    fractaltree(n - 1, length * scale, angle, scale)

    pen.left(angle)
    pen.backward(length)

print("=== FRACTAL TREE MENU ===")

n = int(input("Enter level (n): "))
length = float(input("Enter branch length: "))
angle = float(input("Enter angle: "))
scale = float(input("Enter scale factor: "))

print("n =", n)
print("length =", length)
print("angle =", angle)
print("scale =", scale)

fractaltree(n, length, angle, scale)

turtle.done()