import turtle

wn = turtle.Screen()
wn.title("Cookie Clicker @CodeMaster7000")
wn.bgcolor("navy blue")
wn.register_shape("Cookie.gif")

cookie = turtle.Turtle()
cookie.shape("Cookie.gif")
cookie.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 400)
pen.write(f"Clicks: {clicks}", align="center", font=("Calibri", 28, "normal")) # Customize for your games
def clicked(x, y):
    global clicks
    clicks += 1
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Calibri", 28, "normal")) # Customize for your games
    
cookie.onclick(clicked)
wn.mainloop()