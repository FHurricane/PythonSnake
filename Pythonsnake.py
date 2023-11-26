# Snake eat Orange Game by FastHurricane

import turtle
import time
import random

delay = 0.1

# Punteggio
score = 0
high_score = 0

# Video Setup
wn = turtle.Screen()
wn.title("Snake by FastHurricane")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) 

# Testa del serpente
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Arance
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("orange")
food.penup()
food.goto(0,100)

segments = []


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Punti: 0  - Punteggio Massimo: 0", align="center", font=("Calibri", 24, "normal"))

# Funzioni
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Tasti Bind
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


while True:
    wn.update()

    # Collisioni
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

       
        for segment in segments:
            segment.goto(1000, 1000)
        
       
        segments.clear()

        score = 0

      
        delay = 0.1

        pen.clear()
        pen.write("Punti: {}  Punteggio Massimo: {}".format(score, high_score), align="center", font=("Calibri", 24, "normal")) 


    # Collisioni con arance
    if head.distance(food) < 20:
        # Spawn Arance
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Aggiungi coda al serpente
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

        # delay
        delay -= 0.001

        # Incremento punteggio
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Punti: {}  Punteggio Massimo: {}".format(score, high_score), align="center", font=("Calibri", 24, "normal")) 

  
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

   
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

   
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
           
            for segment in segments:
                segment.goto(1000, 1000)
        
            segments.clear()

            # Reset punteggio
            score = 0

            # Reset delay
            delay = 0.1
        
            # Aggiornamento punteggio
            pen.clear()
            pen.write("Punti: {}  Punteggio Massimo: {}".format(score, high_score), align="center", font=("Calibri", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
