"""
These programs use the turtle to draw images by transformation rules
"""
import turtle
turtle.speed(0)
turtle.delay(0)
turtle.hideturtle()


def drawCell(c, size):  # draws a cell
    colorMap = {0: 'blue', 1: 'yellow', 2: 'orange', 3: 'red'}
    turtle.color('black', colorMap[c])
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.end_fill()


def drawPile(sandpile, size=25):  # uses drawCell to draw a pile
    for x in sandpile:
        turtle.back(3 * size)
        turtle.right(90)
        turtle.forward(size)
        turtle.left(90)
        for y in x:
            drawCell(y, size)
            turtle.forward(size)


def rewrite(word, productions, n):  # performs transformation rules on an input
    z = [word]
    for a in range(n):
        c = ''
        for b in z[a]:
            try:
                c += productions[b]
            except KeyError:
                c += b
        z.append(c)
    return z[n]


def render(word, angle=25, forward=8, position=(0, -300), heading=90):
    stack = []  # translates transformations into instructions for turtle
    for char in word:
        if char == 'F' or char == 'R':
            turtle.forward(forward)
        if char == '-':
            turtle.right(angle)
        if char == '+':
            turtle.left(angle)
        if char == '[':
            stack.append((turtle.position(), turtle.heading()))
        if char == ']':
            position, heading = stack.pop()


def kochSnowflake(n=4):  # forms a Koch Snowflake
     render(rewrite('F++F++F', {'F':'F-F++F-F'}, n),
        angle=60,
        forward=600/3**n,
        position=(-300, -200),
        heading=60)


def fassCurve(n=4):  # forms a Fass Curve
    render(rewrite('F', {'F':'F+R++R-F--FF-R+', 'R':'-F+RR++R+F--F-R'}, n),
        angle=60,
        position=(-300, -200),
        heading=120)
