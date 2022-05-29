import turtle
import tkinter as tk


def square_rectangle_triangle(forward, left):
    t.forward(forward)
    t.left(left)


def do_square():
    t.clear()
    x = 250
    y = 90
    t.fillcolor("green")
    t.begin_fill()
    for i in range(4):
        square_rectangle_triangle(x, y)
    t.end_fill()
    t.home()


def do_rectangle():
    t.clear()
    x_long = 250
    x_short = 150
    y = 90
    t.fillcolor("green")
    t.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            square_rectangle_triangle(x_long, y)
        else:
            square_rectangle_triangle(x_short, y)
    t.end_fill()
    t.home()


def do_circle():
    t.clear()
    t.fillcolor("green")
    t.begin_fill()
    t.circle(100)
    t.end_fill()


def do_triangle():
    t.clear()
    x = 250
    y = 120
    t.fillcolor("green")
    t.begin_fill()
    for i in range(3):
        square_rectangle_triangle(x, y)
    t.end_fill()
    t.home()


def do_interest_thing():
    t.clear()
    t.fillcolor("green")
    t.begin_fill()
    for i in range(3):
        t.forward(500)
        t.left(120)
        t.forward(500)
        t.left(120)
        t.forward(500)
    t.end_fill()
    t.home()


def create_button(text_name, command_name):
    return tk.Button(canvas.master, text=f'{text_name}', command=command_name)


def create_window(position_x, position_y, button_name):
    return canvas.create_window(position_x, position_y, window=button_name)


if __name__ == "__main__":
    screen = turtle.Screen()
    t = turtle.Turtle()
    screen.cv._rootwindow.resizable(False, False)
    screen.title("Geometry")
    screen.setup(600, 600)
    screen.bgcolor("#2471a3")
    canvas = screen.getcanvas()
    create_window(-276, -200, create_button("Square", do_square))
    create_window(-268, -100, create_button("Rectangle", do_rectangle))
    create_window(-279, 0, create_button("Circle", do_circle))
    create_window(-273, 100, create_button("Triangle", do_triangle))
    create_window(-266, 200, create_button("Interesting", do_interest_thing))
    screen.mainloop()
