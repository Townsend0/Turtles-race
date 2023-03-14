from turtle import Turtle,Screen
from random import *
s=Screen()
s.setup(600,500)
d=['red','green','blue','yellow','black','purple']
a=[]
c=-150
for b in range(6):
    a.append(Turtle(shape='turtle'))
    a[b].width(3)
    a[b].color(d[b])
    a[b].penup()
    a[b].goto(-275,c)
    c+=60
e=s.textinput('Make Your Bet','Which turtle would win the race enter a color:\n')
while c:
    for b in range(6):
        a[b].forward(randint(0,5))
        if a[b].xcor()>=275:
            c=False
if e==a[b].pencolor():
    print(f"\nYou win, the {a[b].pencolor()} turtle is the winner")
else:
    print(f"\nYou lose, the {a[b].pencolor()} turtle is the winner")
s.exitonclick()