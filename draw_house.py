import turtle as t


def draw_house():
    """Draw house with garage, 1 door, 4 windows, 2 trees, and 2 clouds on blank canvas.

    Note: Utilizes the turtle graphics package.
    """

    screen = t.Screen()
    screen.setup(1500, 1500)
    screen.setworldcoordinates(0, 0, 1500, 1500)

    # create Turtle Object
    turtle_cursor = t.Turtle()
    turtle_cursor.speed(1000)
    turtle_cursor.penup()

    # draw house with height ~600, width ~500
    x_house = 275
    y_house = 100
    draw_rect(turtle_cursor, x_house, y_house, 500, 600)

    # draw garage with height ~400, width ~300
    x_garage = x_house + 500
    draw_rect(turtle_cursor, x_garage, y_house, 300, 400)

    # draw (2) garage doors on garage
    draw_garage_door(turtle_cursor, x_garage + 40, y_house, 100, 300)
    draw_garage_door(turtle_cursor, x_garage + 160, y_house, 100, 300)

    # draw door on house
    draw_door(turtle_cursor, x_house + 100, y_house, 100, 270)

    # draw three 2nd story windows (same size)
    for i in range(3):
        relative_window_x_pos = 150 * i + 50  # starts 50 from edge of house and 50 between each window
        draw_window(turtle_cursor, x_house + relative_window_x_pos,   y_house + 400, 100, 100)

    # draw one 1st story window (next to door)
    draw_window(turtle_cursor, x_house + 250, y_house + 120, 150, 150)

    # draw two trees (one on each side of house, slightly different heights)
    draw_branches(turtle_cursor, 75, 150, y_house)
    draw_branches(turtle_cursor, 90, 1300, y_house)
    
    # draw two clouds above house
    x_cloud = 300
    y_cloud = 1200
    myFlatCloud(turtle_cursor, x_cloud, y_cloud)
    radius = 50 
    x_bcloud = 900
    y_bcloud = 1300
    myBumpyCloud(turtle_cursor, radius, x_bcloud, y_bcloud, cloud_color="blue")

    # keep screen on until closed by user
    t.mainloop()


def draw_branches(t, branch_length, start_x, start_y):
    t.penup() # lift the pen
    t.goto(start_x, start_y) # place it on x, y
    t.setheading(90) # point the pen upwards
    t.pendown() # put the pen down
    draw_branch(t, branch_length)


def draw_door(cursor, x_pos, y_pos, width, height):
    """
    Draw door at given position of given size.

    :param x_pos: left-most x position of door (in pixels)
    :param y_pos: bottom-most y position of door (in pixels)
    :param width: width of door (in pixels)
    :param height: height of door (in pixels)
    :return: None
    """
    draw_rect(cursor, x_pos, y_pos, width, height)

    # draw doorknob
    cursor.goto(x_pos + width * 4/5, y_pos + height * 1/2)
    cursor.down()
    cursor.circle(width/25)
    cursor.up()


def draw_window(cursor, x_pos, y_pos, width, height):
    """
    Draw window at given position of given size with crossing bars.

    :param cursor: Turtle object
    :param x_pos: left-most x position of window (in pixels)
    :param y_pos: bottom-most y position of window (in pixels)
    :param width: width of window (in pixels)
    :param height: height of window (in pixels)
    :return: None
    """
    draw_rect(cursor, x_pos, y_pos, width, height)

    # draw crossing bars
    draw_single_line(cursor, x_pos, y_pos+height/2, width, 0)
    draw_single_line(cursor, x_pos+width/2, y_pos, height, 90)


def draw_rect(cursor, x_pos, y_pos, width, height):
    """
    Draw rectangle at given position of given size.

    :param cursor: Turtle object
    :param x_pos: left-most x position of rectangle (in pixels)
    :param y_pos: bottom-most y position of rectangle (in pixels)
    :param width: width of rectangle (in pixels)
    :param height: height of rectangle (in pixels)
    :return: None
    """
    cursor.goto(x_pos, y_pos)
    cursor.down()
    cursor.setheading(90)

    for dim in (height, width)*2:
        cursor.forward(dim)
        cursor.right(90)
    cursor.up()


def draw_single_line(cursor, x_start, y_start, length, heading):
    """
    Draw line starting at given coordinates, of given length in direction of given heading.

    :param cursor: Turtle object
    :param x_start: x coordinate for line endpoint
    :param y_start: y coordinate for line endpoint
    :param length: length of line
    :param heading: heading along which to draw line
    :return: None
    """
    cursor.goto(x_start, y_start)
    cursor.setheading(heading)
    cursor.down()
    cursor.forward(length)
    cursor.up()


def draw_branch(t, branch_length):
    if branch_length > 5:
        t.color('brown')
        t.forward(branch_length)

        # save state
        pos = t.position()
        heading = t.heading()

        # draw right branch
        t.right(20)
        draw_branch(t, branch_length - 15)

        # restore state and draw left branch
        t.penup()
        t.goto(pos)
        t.setheading(heading)
        t.pendown()
        t.left(40)
        draw_branch(t, branch_length - 15)

        # restore state
        t.penup()
        t.goto(pos)
        t.setheading(heading)
        t.pendown()
    else:
        # draw leaves if branch short enough
        draw_leaves(t)
        
    t.penup()  # lift the pen


def draw_leaves(t):
    t.penup() # lift the pen
    t.forward(10) # move forward 10
    t.pendown() # put the pen down
    t.color("green") # set the color to green
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    t.color("brown") # reset the color
    t.right(180) # turn right 180 degrees
    t.penup() # lift the pen
    t.forward(10) # move forward 10    
    t.pendown() # put the pen down


def draw_garage_door(t, start_x, start_y, width, height):
    t.penup() # lift the pen
    t.goto(start_x, start_y) # place it on x, y
    t.setheading(0) # point the pen right
    t.pendown() # put the pen down
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    for i in range(1, 11):
        t.penup()
        t.goto(start_x, start_y + i * height / 10)
        t.pendown()
        t.forward(width)

    t.up()


def myFlatCloud(my_turtle, x_cloud, y_cloud):
    my_turtle.pu()
    my_turtle.setheading(0)
    my_turtle.setpos(x_cloud,y_cloud)
    my_turtle.pd()
    my_turtle.color('blue')
    my_turtle.forward(150)
    my_turtle.left(90)
    turt_pos = my_turtle.pos()
    my_turtle.forward(30)

    for i in range (1,3):
        for i in range(1,15):
            my_turtle.left(10)
            my_turtle.forward(10)
        my_turtle.left(210)

        for i in range(1,20):
            my_turtle.left(10)
            my_turtle.forward(10) 
        my_turtle.left(190)
    my_turtle.left(160)
    current_pos = my_turtle.pos()
    my_turtle.forward((current_pos[1]-turt_pos[1]))
    my_turtle.left(90)
    my_turtle.forward((turt_pos[0]-current_pos[0]))


def ellipse(my_turtle, radius, color):
    my_turtle.color(color,color)
    my_turtle.begin_fill()
    for i in range(2):
        my_turtle.circle(radius,90)
        my_turtle.circle(radius//2,90)
    my_turtle.end_fill()


def myBumpyCloud(my_turtle, radius, x_cloud, y_cloud, cloud_color="blue"):
    my_turtle.pu()
    my_turtle.setheading(0)
    my_turtle.setpos(x_cloud,y_cloud)
    my_turtle.pd()
    ellipse(my_turtle, radius,cloud_color)
    my_turtle.forward(radius)
    for i in range(1,7):
        ellipse(my_turtle, radius,cloud_color)
        my_turtle.right(60)


if __name__ == '__main__':
    draw_house()
