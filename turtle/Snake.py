import turtle

def drawSnake(rad, angle, len, neckrad):
    for i in range(len) :
        turtle.pencolor("green")
        turtle.circle(rad, angle)
        turtle.pencolor("blue") 
        turtle.circle(-rad, angle)
    turtle.circle (rad, angle/2)
    turtle.pencolor("blue")
    turtle.circle (neckrad*5,180)
    turtle.seth(140)
    for i in range(len) :
        turtle.pencolor("green")
        turtle.circle(rad, angle)
        turtle.pencolor("blue") 
        turtle.circle(-rad, angle)
    turtle.pencolor("red")
    turtle.circle (neckrad*10,300)
    
    

def main():
    turtle.setup(1300,800,0,0)
    pythonsize = 20
    turtle.pensize(pythonsize)
    turtle.seth(-40)
    drawSnake(40,80,4,pythonsize/2)
    
main()
