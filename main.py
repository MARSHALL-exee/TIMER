import turtle


from clock import Clock, win, toggle_pause, times_up_beeps

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Timer")
screen.tracer(0)

clock = Clock()

# Bind the key press event to the function
win.listen()
win.onkeypress(toggle_pause, "space")
'''win.winsound.Beep(2000, 2000)'''
win.winsound.Beep(1000, 500)
win.winsound.Beep(1500, 300)

screen.exitonclick()
