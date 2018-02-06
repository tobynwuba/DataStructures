import turtle

def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen*0.75,t)
        t.left(40)
        tree(branchLen*0.75,t)
        t.color("green")
        t.right(20)
        t.backward(branchLen)
        t.color("black")

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("black")
    tree(75,t)
    myWin.exitonclick()

main()
