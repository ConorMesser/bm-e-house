import turtle as t


def draw_house(world_width, world_height, skip_trees=False):
    """Draw house with garage, 1 door, 4 windows, 2 trees, and 2 clouds on blank canvas.

    :param world_width: width of world (in pixels)
    :param world_height: height of world (in pixels)
    :param skip_trees: optional boolean parameter to skip drawing trees, to speed up graphics (default False)

    Note: Utilizes the turtle graphics package.
    """
    # set up screen
    screen = t.Screen()
    screen.setup(world_width, world_height)
    screen.setworldcoordinates(0, 0, world_width, world_height)

    # create Turtle object
    my_turtle = t.Turtle()
    my_turtle.speed("fastest")
    my_turtle.penup()

    # draw house
    x_house = 1/5 * world_width
    y_house = 1/15 * world_height
    draw_rect(my_turtle, x_house, y_house, 1/3 * world_width, 6/15 * world_height)

    # draw garage
    x_garage = x_house + 1/3 * world_width
    draw_rect(my_turtle, x_garage, y_house, 1/5 * world_width, 4/15 * world_height)

    # draw (2) garage doors on garage
    draw_garage_door(my_turtle, x_garage + 0.03 * world_width, y_house, 1/15 * world_width, 3/15 * world_height)
    draw_garage_door(my_turtle, x_garage + 0.1 * world_width, y_house, 1/15 * world_width, 3/15 * world_height)

    # draw door on house
    draw_door(my_turtle, x_house + 1/15 * world_width, y_house, 1/15 * world_width, 1/5 * world_height, world_width)

    # draw three 2nd story windows (same size)
    for i in range(3):
        relative_window_x_pos = 1/10 * world_width * i + 1/30 * world_width
        draw_window(my_turtle, x_house + relative_window_x_pos, y_house + 4/15 * world_height, 1/15 * world_width, 1/15 * world_height)

    # draw one 1st story window (next to door)
    draw_window(my_turtle, x_house + 1/6 * world_width, y_house + 1/10 * world_height, 1/10 * world_width, 1/10 * world_height)

    # draw two trees (one on each side of house, slightly different heights)
    if not skip_trees:
        draw_branches(my_turtle, 3/60 * world_width, 1/10 * world_width, y_house, world_width, "brown", "green")
        draw_branches(my_turtle, 3/50 * world_width, 13/15 * world_width, y_house, world_width, "brown", "green")
    
    # draw two clouds above house
    x_cloud = 1/5 * world_width
    y_cloud = 4/5 * world_height
    draw_flat_cloud(my_turtle, x_cloud, y_cloud, world_width)
    radius = 1/30 * world_width
    x_bcloud = 9/15 * world_width
    y_bcloud = 13/15 * world_height
    draw_bumpy_cloud(my_turtle, world_width, radius, x_bcloud, y_bcloud, cloud_color="blue")

    # keep screen on until closed by user
    t.mainloop()


def draw_branches(my_turtle, branch_length, x_pos, y_pos, world_width, color_branch, color_leaves):
    """
    Draw branches at given position of given branch_length.

    :param my_turtle: turtle cursor
    :param branch_length: branch_length (in pixels)
    :param start_x: left-most x position of first branch (in pixels)
    :param start_y: bottom-most y position of first branch (in pixels)
    :return: None
    """
    my_turtle.penup()
    my_turtle.goto(x_pos, y_pos)
    my_turtle.setheading(90)
    my_turtle.pendown()
    draw_branch(my_turtle, branch_length, world_width, color_branch, color_leaves)


def draw_branch(my_turtle, branch_length, world_width, color_branch, color_leaves):
    """
    Draw branches off of initial branch recursively.

    :param my_turtle: turtle cursor
    :param branch_length: branch_length (in pixels)
    """
    if branch_length > 1/300 * world_width:
        my_turtle.color(color_branch)
        my_turtle.forward(branch_length)
        # save state
        pos = my_turtle.position()
        heading = my_turtle.heading()
        # draw right branch
        my_turtle.right(2/150 * world_width)
        draw_branch(my_turtle, branch_length - 1/100 * world_width, world_width, color_branch, color_leaves)
        # restore state and draw left branch
        my_turtle.penup()
        my_turtle.goto(pos)
        my_turtle.setheading(heading)
        my_turtle.pendown()
        my_turtle.left(4/150 * world_width)
        draw_branch(my_turtle, branch_length - 1/100 * world_width, world_width, color_branch, color_leaves)
        # restore state
        my_turtle.penup()
        my_turtle.goto(pos)
        my_turtle.setheading(heading)
        my_turtle.pendown()
    else:
        # draw leaves if branch short enough
        draw_leaves(my_turtle, color_branch, color_leaves, world_width)
    my_turtle.penup()

def draw_leaves(my_turtle, color_branch, color_leaves, world_width):
    """
    Draw leaves off of smallest last branch.

    :param my_turtle: turtle cursor
    """
    my_turtle.penup()
    my_turtle.forward(1/150 * world_width)
    my_turtle.pendown()
    my_turtle.color(color_leaves)
    my_turtle.begin_fill()
    my_turtle.circle(1/300 * world_width)
    my_turtle.end_fill()
    my_turtle.color(color_branch)
    my_turtle.right(18/150 * world_width)
    my_turtle.penup()
    my_turtle.forward(1/150 * world_width)
    my_turtle.pendown()


def draw_door(my_turtle, x_pos, y_pos, width, height, world_width):
    """
    Draw door at given position of given size.

    :param x_pos: left-most x position of door (in pixels)
    :param y_pos: bottom-most y position of door (in pixels)
    :param width: width of door (in pixels)
    :param height: height of door (in pixels)
    :return: None
    """
    draw_rect(my_turtle, x_pos, y_pos, width, height)

    # draw doorknob
    my_turtle.goto(x_pos + width * 4/5, y_pos + height * 1/2)
    my_turtle.down()
    my_turtle.circle(width/(1/60 * world_width))
    my_turtle.up()


def draw_window(my_turtle, x_pos, y_pos, width, height):
    """
    Draw window at given position of given size with crossing bars.

    :param my_turtle: Turtle object
    :param x_pos: left-most x position of window (in pixels)
    :param y_pos: bottom-most y position of window (in pixels)
    :param width: width of window (in pixels)
    :param height: height of window (in pixels)
    :return: None
    """
    draw_rect(my_turtle, x_pos, y_pos, width, height)

    # draw crossing bars
    draw_single_line(my_turtle, x_pos, y_pos+height/2, width, 0)
    draw_single_line(my_turtle, x_pos+width/2, y_pos, height, 90)


def draw_rect(my_turtle, x_pos, y_pos, width, height):  # todo test
    """
    Draw rectangle at given position of given size.

    :param my_turtle: Turtle object
    :param x_pos: left-most x position of rectangle (in pixels)
    :param y_pos: bottom-most y position of rectangle (in pixels)
    :param width: width of rectangle (in pixels)
    :param height: height of rectangle (in pixels)
    :return: None
    """
    my_turtle.goto(x_pos, y_pos)
    my_turtle.down()
    my_turtle.setheading(90)  # todo add as input? with default

    for dim in (height, width)*2:  # todo make clearer
        my_turtle.forward(dim)
        my_turtle.right(90)
    my_turtle.up()


def draw_single_line(my_turtle, x_start, y_start, length, heading):  # todo test
    """
    Draw line starting at given coordinates, of given length in direction of given heading.

    :param my_turtle: Turtle object
    :param x_start: x coordinate for line endpoint
    :param y_start: y coordinate for line endpoint
    :param length: length of line
    :param heading: heading along which to draw line
    :return: None
    """
    my_turtle.goto(x_start, y_start)
    my_turtle.setheading(heading)
    my_turtle.down()
    my_turtle.forward(length)
    my_turtle.up()


def draw_garage_door(my_turtle, start_x, start_y, width, height):
    my_turtle.penup()
    my_turtle.goto(start_x, start_y)
    my_turtle.setheading(0)
    my_turtle.pendown()
    for _ in range(2):
        my_turtle.forward(width)
        my_turtle.left(90)
        my_turtle.forward(height)
        my_turtle.left(90)

    for i in range(1, 11):
        my_turtle.penup()
        my_turtle.goto(start_x, start_y + i * (height / 10))
        my_turtle.pendown()
        my_turtle.forward(width)

    my_turtle.up()


def draw_flat_cloud(my_turtle, x_cloud, y_cloud, world_width):
    my_turtle.pu()
    my_turtle.setheading(0)
    my_turtle.setpos(x_cloud,y_cloud)
    my_turtle.pd()
    my_turtle.color("blue")
    my_turtle.forward(1/10 * world_width)
    my_turtle.left(9/150 * world_width)
    turt_pos = my_turtle.pos()
    my_turtle.forward(3/150 * world_width)

    for i in range (1,3):
        for i in range(1,15):
            my_turtle.left(1/150 * world_width)
            my_turtle.forward(1/150 * world_width)
        my_turtle.left(21/150 * world_width)

        for i in range(1,20):
            my_turtle.left(1/150 * world_width)
            my_turtle.forward(1/150 * world_width)
        my_turtle.left(19/150 * world_width)
    my_turtle.left(16/150 * world_width)
    current_pos = my_turtle.pos()
    my_turtle.forward((current_pos[1]-turt_pos[1]))
    my_turtle.left(9/150 * world_width)
    my_turtle.forward((turt_pos[0]-current_pos[0]))


def ellipse(my_turtle, radius, color, world_width):  # todo add second radius input?
    my_turtle.color(color,color)
    my_turtle.begin_fill()
    for i in range(2):
        my_turtle.circle(radius,(9/150 * world_width))
        my_turtle.circle(radius//2,(9/150 * world_width))
    my_turtle.end_fill()


def draw_bumpy_cloud(my_turtle, world_width, radius, x_cloud, y_cloud, cloud_color="blue"):
    my_turtle.pu()
    my_turtle.setheading(0)
    my_turtle.setpos(x_cloud, y_cloud)
    my_turtle.pd()
    ellipse(my_turtle, radius, cloud_color, world_width)
    my_turtle.forward(radius)
    for i in range(1,7):
        ellipse(my_turtle, radius, cloud_color, world_width)
        my_turtle.right(60)


if __name__ == '__main__':
    draw_house(1500, 1500)
