import turtle as t 

#Set background color 
t.screensize(1500,1500,"white")

#Create my turtle
my_turtle = t.Turtle()
my_turtle.color("black")
my_turtle.shape("turtle")
my_turtle.speed(20)


#Create a rectangle function for the house and garage. Inputs: starting location (x, y), height & width (h, w)
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

def myBumpyCloud(radius, cloud_color="blue"):
    ellipse(radius,cloud_color)
    t.forward(radius)
    for i in range(1,7):
        ellipse(radius,cloud_color)
        t.right(60)

t.mainloop()