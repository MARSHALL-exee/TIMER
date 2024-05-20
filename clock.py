''' import turtle
import time

# Set up the screen
win = turtle.Screen()
win.bgcolor("white")
win.title("Timer")

# Create a turtle to draw the timer
timer = turtle.Turtle()
timer.speed(0)
timer.color("black")
timer.hideturtle()

# Function to draw the timer
def draw_timer(t):
    timer.clear()
    timer.penup()
    timer.goto(0, 0)
    timer.pendown()
    timer.write(f"Time: {t:02d} seconds", align="center", font=("Arial", 24, "normal"))

# Global variables
Pause = False
RemainingTime = 90  # Default countdown time

# Function to toggle pause state
def toggle_pause():
    global Pause
    Pause = not Pause
    if not Pause:
        countdown(RemainingTime)  # Resume countdown with remaining time

# Function to restart the countdown
def restart():
    global Pause, RemainingTime
    Pause = False
    RemainingTime = 90
    countdown(RemainingTime)

# Function to countdown
def countdown(t):
    global Pause, RemainingTime
    while t >= 0:
        if Pause:
            RemainingTime = t
            break
        draw_timer(t)
        time.sleep(1)
        t -= 1
    if t < 0:
        timer.clear()
        timer.write("Time Up!!", align="center", font=("Arial", 24, "normal"))

# Bind the key press events to the functions
win.listen()
win.onkeypress(toggle_pause, "space")
win.onkeypress(restart, "r")

# Start the initial countdown
countdown(RemainingTime)

# Keep the window open
turtle.done()'''

'''import turtle
import time
import winsound

# Set up the screen
win = turtle.Screen()
win.bgcolor("white")
win.title("Timer")

# Create a turtle to draw the timer
timer = turtle.Turtle()
timer.speed(0)
timer.color("black")
timer.hideturtle()

# Function to draw the timer
def draw_timer(t):
    timer.clear()
    timer.penup()
    timer.goto(0, 0)
    timer.pendown()
    timer.write(f"Time: {t:02d} seconds", align="center", font=("Arial", 24, "normal"))

# Global variables
Pause = False
RemainingTime = 10  # Default countdown time

# Function to toggle pause state
def toggle_pause():
    global Pause
    Pause = not Pause
    if not Pause:
        countdown(RemainingTime)  # Resume countdown with remaining time

# Function to restart the countdown
def restart():
    global Pause, RemainingTime
    Pause = False
    RemainingTime = 10
    countdown(RemainingTime)

# Function to countdown
def countdown(t):
    global Pause, RemainingTime
    while t >= 0:
        if Pause:
            RemainingTime = t
            break
        draw_timer(t)
        time.sleep(1)
        t -= 1
    if t < 0:
        timer.clear()
        timer.write("Time Up!!", align="center", font=("Arial", 24, "normal"))
        winsound.Beep(2000, 2000)  # Frequency of 1000 Hz for 1 second

# Bind the key press events to the functions
win.listen()
win.onkeypress(toggle_pause, "space")
win.onkeypress(restart, "r")

# Start the initial countdown
countdown(RemainingTime)

# Keep the window open
turtle.done()'''

import turtle
import time
import winsound

# Set up the screen
win = turtle.Screen()
win.bgcolor("white")
win.title("Timer")

# Create a turtle to draw the timer
timer = turtle.Turtle()
timer.speed(0)
timer.color("black")
timer.hideturtle()

# Function to draw the timer
def draw_timer(t):
    timer.clear()
    timer.penup()
    timer.goto(0, 0)
    timer.pendown()
    timer.write(f"Time: {t:02d} seconds", align="center", font=("Arial", 24, "normal"))

# Global variables
Pause = False
RemainingTime = int(input("Enter countdown: ")) # countdown time

# Function to toggle pause state
def toggle_pause():
    global Pause
    Pause = not Pause
    if not Pause:
        countdown(RemainingTime)  # Resume countdown with remaining time

# Function to restart the countdown
def restart():
    global Pause, RemainingTime
    Pause = False
    countdown(RemainingTime)

# Function to play "Time's Up!" sound using a sequence of beeps
def times_up_beeps():
    for _ in range(3):
        winsound.Beep(1000, 500)  # 1000 Hz for 500 milliseconds
        time.sleep(0.1)           # Short pause between beeps
    for _ in range(3):
        winsound.Beep(1500, 300)  # 1500 Hz for 300 milliseconds
        time.sleep(0.1)

# Function to countdown
def countdown(t):
    global Pause, RemainingTime
    while t >= 0:
        if Pause:
            RemainingTime = t
            break
        draw_timer(t)
        time.sleep(1)
        t -= 1
    if t < 0:
        timer.clear()
        timer.write("Time Up!!", align="center", font=("Arial", 24, "normal"))
        times_up_beeps()

# Bind the key press events to the functions
win.listen()
win.onkeypress(toggle_pause, "space")
win.onkeypress(restart, "r")

# Start the initial countdown
countdown(RemainingTime)

# Keep the window open
turtle.done()
