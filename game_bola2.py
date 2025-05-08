# -*- coding: utf-8 -*-
"""
Created on Thu May  8 09:51:14 2025

@author: office
"""

import turtle
import random
import time

# Inisialisasi layar
wn = turtle.Screen()
wn.title("Hujan Bola Durian")
wn.bgcolor("lightgreen")
wn.setup(width=600, height=600)
wn.tracer(0)

# Pemain (bola biru)
player = turtle.Turtle()
player.shape("circle")
player.color("blue")
player.penup()
player.speed(0)
player.goto(0, -250)
player.direction = "stop"

# Skor
score = 0
lives = 3
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Skor: {score}  Nyawa: {lives}", align="center", font=("Courier", 24, "normal"))

# Daftar bola duri
spiky_balls = []
for _ in range(10):
    spiky_ball = turtle.Turtle()
    spiky_ball.shape("circle")
    spiky_ball.color("red")
    spiky_ball.penup()
    spiky_ball.speed(0)
    spiky_ball.shapesize(random.uniform(0.5, 2), random.uniform(0.5, 2))
    spiky_ball.goto(random.randint(-280, 280), random.randint(350, 600))
    spiky_ball.dy = random.uniform(1, 3)
    spiky_balls.append(spiky_ball)

# Daftar kado
gifts = []
for _ in range(5):
    gift = turtle.Turtle()
    gift.shape("square")
    gift.color(random.choice(["yellow", "orange", "purple", "pink"]))
    gift.penup()
    gift.speed(0)
    gift.shapesize(stretch_wid=1, stretch_len=1)
    gift.goto(random.randint(-280, 280), random.randint(350, 600))
    gift.dy = random.uniform(0.5, 2)
    gifts.append(gift)

# Fungsi untuk menggerakkan pemain
def move_left():
    player.direction = "left"

def move_right():
    player.direction = "right"

# Binding keyboard
wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Loop utama game
while True:
    wn.update()

    # Gerakkan pemain
    if player.direction == "left":
        player.setx(player.xcor() - 20)
    if player.direction == "right":
        player.setx(player.xcor() + 20)

    # Batas pemain
    if player.xcor() < -280:
        player.setx(-280)
    if player.xcor() > 280:
        player.setx(280)

    # Gerakkan bola duri
    for ball in spiky_balls:
        ball.sety(ball.ycor() - ball.dy)

        # Reset bola duri jika keluar layar
        if ball.ycor() < -300:
            ball.goto(random.randint(-280, 280), random.randint(350, 600))
            ball.dy = random.uniform(1, 3)

        # Deteksi tabrakan dengan pemain
        if player.distance(ball) < 20 * ball.shapesize()[0]:
            lives -= 1
            score_display.clear()
            score_display.write(f"Skor: {score}  Nyawa: {lives}", align="center", font=("Courier", 24, "normal"))
            ball.goto(random.randint(-280, 280), random.randint(350, 600))
            ball.dy = random.uniform(1, 3)

            if lives == 0:
                score_display.clear()
                score_display.write(f"GAME OVER! Skor Akhir: {score}", align="center", font=("Courier", 24, "normal"))
                time.sleep(2)
                wn.bye()

    # Gerakkan kado
    for gift in gifts:
        gift.sety(gift.ycor() - gift.dy)

        # Reset kado jika keluar layar
        if gift.ycor() < -300:
            gift.goto(random.randint(-280, 280), random.randint(350, 600))
            gift.dy = random.uniform(0.5, 2)
            gift.color(random.choice(["yellow", "orange", "purple", "pink"]))

        # Deteksi tabrakan dengan pemain
        if player.distance(gift) < 20:
            score += 10
            score_display.clear()
            score_display.write(f"Skor: {score}  Nyawa: {lives}", align="center", font=("Courier", 24, "normal"))
            gift.goto(random.randint(-280, 280), random.randint(350, 600))
            gift.dy = random.uniform(0.5, 2)
            gift.color(random.choice(["yellow", "orange", "purple", "pink"]))

wn.mainloop()