import turtle as t

t.clearscreen()
t.bgcolor("grey")
screen = t.Screen()
animal = t.Turtle()
animal.speed(0)


def triangle(animal, size, order):
    if order == 0:
        animal.forward(size)
    else:
        for i in [-120, -120, -120]:
            animal.left(i)
            triangle(animal, size / 3, order - 1)
            animal.left(-120)
            animal.forward(size / 3)


triangle(animal, 900, 4)
screen.exitonclick()
