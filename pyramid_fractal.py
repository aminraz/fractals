import turtle as t

t.clearscreen()
t.bgcolor("grey")
animal = t.Turtle()
animal.speed(0)


def r_cube(animal, size, order):
    if order == 0:
        animal.forward(size)
    else:
        for i in [90, -90, -90, 90, 0]:
            r_cube(animal, size / 4, order - 1)
            animal.left(i)


r_cube(animal, 3000, 5)
