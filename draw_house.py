import turtle as t


def draw_house():
    """Draw house with garage, 1 door, 4 windows, 2 trees, and 2 clouds on blank canvas.

    Note: Utilizes the turtle graphics package.
    """
    t.screensize(1500, 1500)

    # create Turtle Object
    turtle_cursor = t.Turtle()

    # draw house with height ~600, width ~500

    # draw garage with height ~400, width ~300

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

if __name__ == '__main__':
    draw_house()

