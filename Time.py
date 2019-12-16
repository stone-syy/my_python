#SevenDigitsDrawV2.py
import turtle
import time
def drawGap(): #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '$':
            turtle.write('时', font=("Arial", 18, "normal"))
            turtle.pencolor("red")
            turtle.fd(40)
        elif i == '@':
            turtle.write('分', font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '*':
            turtle.write('秒', font=("Arial", 18, "normal"))
            turtle.pencolor("red")
        else:
            drawDigit(eval(i))
def main():
    turtle.setup(1500, 800, 10, 10)
    turtle.penup()
    turtle.goto(0,100)
    turtle.write('源源报时:', font=("Arial", 35, "normal"))
    turtle.goto(0, 0)
    turtle.fd(-600)
    turtle.pensize(5)
#    drawDate('2018-10=10+')
    drawDate(time.strftime('%Y-%m=%d+%H$%M@%S*', time.localtime()))
    turtle.hideturtle()
    turtle.done()
main()
#print(time.strftime("%Y-%m=%d %H:%M:%", time.gmtime()))