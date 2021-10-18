from turtle import*
from math import *
import matplotlib.pyplot as plt

ø = 0
speed(0)
hideturtle()
ex = []
why = []
while ø <= 360:

    ç = radians(ø)

    const = ç-radians(360)
    if ø <= 360:
        r = (sqrt(2))+(2*sin(ç))

        if ø == 0:
            penup()
            x = r*cos(ç)
            y = r*sin(ç)
        else:
            pendown()
            if ø <= 90:
                x = r*cos(ç)
                y = r*sin(ç)

            elif ø <= 180:
                x = -r*cos(radians(180)-ç)
                y = r*sin(radians(180)-ç)
            elif ø <= 270:
                x = -r*cos(ç-radians(180))
                y = -r*sin(ç-radians(180))
            elif ø <= 360:
                x = r*cos(radians(360)-ç)
                y = -r*sin(radians(360)-ç)
    elif ø <= 720:
        r = (cos(const))**2

        if const <= 90:
            x = -r*cos(const)
            y = -r*sin(const)

        elif const <= 180:
            x = r*cos(radians(180)-const)
            y = -r*sin(radians(180)-const)
        elif const <= 270:
            x = r*cos(const-radians(180))
            y = r*sin(const-radians(180))
        elif const <= 360:
            x = -r*cos(radians(360)-const)
            y = r*sin(radians(360)-const)
    else:
        ø = 0

    print(x, ' ', y, ' ', 'angle', ø)

    setpos(x, y)

    ex.append(x)
    why.append(y)

    ø += 1
plt.plot(ex, why)
plt.show()
onclick()
