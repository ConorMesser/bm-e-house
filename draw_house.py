import turtle as t


def draw_house():
    """Draw house with garage, 1 door, 4 windows, 2 trees, and 2 clouds on blank canvas.

    Note: Utilizes the turtle graphics package.
    """
    t.screensize(1500, 1500)
    house_x = 50
    house_y = 300

    # draw house with height ~600, width ~500

    # draw garage with height ~400, width ~300

    # draw (2) garage doors on garage

    # draw door on house
    draw_door(house_x + 100, house_y, 100, 270)

    # draw three 2nd story windows (same size)
    for i in range(3):
        relative_window_x_pos = 150 * i + 50  # starts 50 from edge of house and 50 between each window
        draw_window(house_x + relative_window_x_pos,400, 100, 100)

    # draw one 1st story window (next to door)
    draw_window(house_x + 250, 120, 150, 150)

    # draw two trees (one on each side of house, slightly different heights)

    # draw two clouds above house

    t.mainloop()


def draw_door(x_pos, y_pos, width, height):
    """
    Draw door at given position of given size.

    :param x_pos: left-most x position of door (in pixels)
    :param y_pos: bottom-most y position of door (in pixels)
    :param width: width of door (in pixels)
    :param height: height of door (in pixels)
    :return: None
    """
    draw_rect(x_pos, y_pos, width, height)

    # draw doorknob
    t.goto(x_pos + width * 4/5, y_pos + height * 1/2)
    t.down()
    t.circle(width/50)
    t.up()


def draw_window(x_pos, y_pos, width, height):
    """
    Draw window at given position of given size with crossing bars.

    :param x_pos: left-most x position of window (in pixels)
    :param y_pos: bottom-most y position of window (in pixels)
    :param width: width of window (in pixels)
    :param height: height of window (in pixels)
    :return: None
    """
    draw_rect(x_pos, y_pos, width, height)

    # draw crossing bars
    draw_single_line(x_pos, y_pos+height/2, width, 0)
    draw_single_line(x_pos+width/2, y_pos, height, 90)


def draw_rect(x_pos, y_pos, width, height):
    """
    Draw rectangle at given position of given size.

    :param x_pos: left-most x position of rectangle (in pixels)
    :param y_pos: bottom-most y position of rectangle (in pixels)
    :param width: width of rectangle (in pixels)
    :param height: height of rectangle (in pixels)
    :return: None
    """
    t.goto(x_pos, y_pos)
    t.down()
    t.setheading(90)

    for dim in (height, width)*2:
        t.forward(dim)
        t.right(90)
    t.up()


def draw_single_line(x_start, y_start, length, heading):
    """
    Draw line starting at given coordinates, of given length in direction of given heading.

    :param x_start: x coordinate for line endpoint
    :param y_start: y coordinate for line endpoint
    :param length: length of line
    :param heading: heading along which to draw line
    :return: None
    """
    t.goto(x_start, y_start)
    t.down()
    t.forward(length)
    t.up()


if __name__ == '__main__':
    draw_house()
