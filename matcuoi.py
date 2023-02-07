#import library
import turtle

#Setting pensize and color of pen
turtle.pensize(6)
turtle.pencolor("Black")

#Draw the circle
facesize = 200
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.circle(facesize)

#Vẽ mắt bằng hai hình tròn và tô màu dỏ tương ứng cho mắt
#1 Màu nền mắt là màu dỏ
turtle.fillcolor("Purple")
turtle.penup()
turtle.goto(-70,90)
turtle.pendown()

#2 Khai báo biến eyesize lưu kích thước mắt
eye_size = 17.5

turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()
turtle.penup()

turtle.goto(70,90)
turtle.pendown()
turtle.begin_fill()
turtle.circle(eye_size)
turtle.end_fill()

#Vẽ hình tam giác cho mũi
turtle.fillcolor("Red")
turtle.penup()
turtle.goto(0,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(-30, steps=3)
turtle.end_fill()

#Vẽ miệng cười bằng nửa hình tròn
turtle.penup()
turtle.goto(-100,15)
turtle.pendown()
turtle.right(90)
turtle.circle(100,180)
turtle.mainloop()