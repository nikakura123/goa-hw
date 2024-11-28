from turtle import *
width(7)
color("pink")
speed(20)

forward(200)
begin_fill()
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200) #end of square
left(90)
end_fill()



forward(70)   #drawing a door
color("skyblue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()

color("skyblue") #painting a roof
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("pink")
left(30)
forward(50)
color("skyblue") #painting a window
begin_fill()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


penup()
goto(200,150)
pendown()

left(90)    #painting a window
begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

 







exitonclick()