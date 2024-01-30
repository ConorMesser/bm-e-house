import os
from PIL import Image
import turtle as t
from draw_house import draw_house


def gen_house_image():
    draw_house(900, 700, keep_window_open=False)

    save_turtle_image('test_house')


def gen_rect_image():
    t.setup(900, 700)
    t.screensize(900, 700)

    t.penup()
    t.goto(20, 20)
    t.setheading(90)
    t.pendown()
    t.forward(40)
    for _ in range(3):
        t.right(90)
        t.forward(40)

    t.hideturtle()
    save_turtle_image('test_rect')

def gen_line_image():
    t.setup(900, 700)
    t.screensize(900, 700)

    t.setheading(90)
    t.pendown()
    t.forward(100)

    t.hideturtle()
    save_turtle_image('test_line')


def save_turtle_image(filename):
    actual_ps = os.path.join('./nm_test_data', f'{filename}.ps')
    actual_png = os.path.join('./nm_test_data', f'{filename}.png')
    canvas = t.getcanvas()
    canvas.postscript(file=actual_ps)
    with Image.open(actual_ps) as im:
        im.save(actual_png)


if __name__ == '__main__':
    gen_rect_image()
    t.clearscreen()

    gen_line_image()
    t.clearscreen()

    gen_house_image()
    t.clearscreen()

