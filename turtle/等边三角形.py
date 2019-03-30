import  turtle
def main():
    turtle.setup(1300,800,0,0)
    pythonsize = 20
    turtle.pensize(pythonsize)
    
    turtle.pencolor("blue")
    turtle.fd(120)
    turtle.seth(120)
    turtle.pencolor("red")
    turtle.fd(120)
    turtle.seth(-120)
    turtle.pencolor("yellow")
    turtle.fd(120)

main()
