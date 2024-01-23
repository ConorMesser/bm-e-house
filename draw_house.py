import turtle as t


def draw_house():
    """Draw house with garage, 1 door, 4 windows, 2 trees, and 2 clouds on blank canvas.

    Note: Utilizes the turtle graphics package.
    """
    screen = t.Screen()
    screen.setup(1500, 1500)

    # create Turtle Object
    turtle_cursor = t.Turtle()
    turtle_cursor.speed(100)

    # draw house with height ~600, width ~500
    x_rect1 = 0
    y_rect1 = 0
    drawRectangle(turtle_cursor, x_rect1, y_rect1, 600, 500)
    # draw garage with height ~400, width ~300
    x_rect2 = 500
    y_rect2 = 0
    drawRectangle(turtle_cursor, x_rect2, y_rect2, 400, 300)

    # draw (2) garage doors on garage
    draw_garage_door(turtle_cursor, 50, -50, 100, 100)
    draw_garage_door(turtle_cursor, 160, -50, 100, 100)

    # draw door on house

    # draw three 2nd story windows (same size)

    # draw one 1st story window (next to door)

    # draw two trees (one on each side of house, slightly different heights)
    draw_branches(turtle_cursor, 75, -600, 0)
    draw_branches(turtle_cursor, 75, 600, 0)
    
    # draw two clouds above house
    x_cloud = 800
    y_cloud = 800
    myFlatCloud(turtle_cursor, x_cloud, y_cloud)
    radius = 50 
    x_bcloud = -800
    y_bcloud = 800
    myBumpyCloud(turtle_cursor, radius, x_bcloud, y_bcloud, cloud_color="blue")

    t.mainloop()

def draw_branches(t, branch_length, start_x, start_y):
    t.penup() # lift the pen
    t.goto(start_x, start_y) # place it on x, y
    t.setheading(90) # point the pen upwards
    t.pendown() # put the pen down
    draw_branch(t, branch_length)

def draw_branch(t, branch_length):
    if branch_length > 5:
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
        
    t.penup() # lift the pen

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
def drawRectangle(my_turtle, x_rect, y_rect, h, w):
    my_turtle.pu()
    my_turtle.setpos(x_rect,y_rect)
    my_turtle.pd()
    my_turtle.forward(w)
    my_turtle.left(90)
    my_turtle.forward(h)
    my_turtle.left(90)
    my_turtle.forward(w)
    my_turtle.left(90)
    my_turtle.forward(h)
    my_turtle.pu()

def myFlatCloud(my_turtle, x_cloud, y_cloud):
    my_turtle.pu()
    my_turtle.setpos(x_cloud,y_cloud)
    my_turtle.pd()
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
    #print((current_pos[1]-turt_pos[1]))
    my_turtle.forward((current_pos[1]-turt_pos[1]))
    my_turtle.left(90)
    my_turtle.forward((turt_pos[0]-current_pos[0]))

def ellipse(radius, color):
    t.color(color,color)
    t.begin_fill()
    for i in range(2):
        t.circle(radius,90)
        t.circle(radius//2,90)
    t.end_fill()

def myBumpyCloud(my_turtle, radius, x_cloud, y_cloud, cloud_color="blue"):
    my_turtle.pu()
    my_turtle.setpos(x_cloud,y_cloud)
    my_turtle.pd()
    ellipse(radius,cloud_color)
    t.forward(radius)
    for i in range(1,7):
        ellipse(radius,cloud_color)
        t.right(60)

if __name__ == '__main__':
    draw_house()

