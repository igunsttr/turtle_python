# -*- coding: utf-8 -*-
"""
Created on Thu May  8 09:33:27 2025

@author: office
"""

import turtle
import random

# Inisialisasi layar
screen = turtle.Screen()
screen.setup(width=600, height=700)
screen.bgcolor("lightblue")
screen.tracer(0)  # Menonaktifkan update layar otomatis

# Bola yang dapat dikontrol
player_ball = turtle.Turtle()
player_ball.shape("circle")
player_ball.color("red")
player_ball.penup()
player_ball.goto(0, -250)
player_ball.speed(0)

# Daftar untuk menyimpan bola berduri
spiky_balls = []

# Fungsi untuk membuat bola berduri baru
def create_spiky_ball():
    spiky_ball = turtle.Turtle()
    spiky_ball.shape("circle")
    spiky_ball.color("green")
    # Membuat "duri" dengan beberapa lingkaran kecil
    for _ in range(8):
        spike = turtle.Turtle()
        spike.shape("circle")
        spike.color("black")
        spike.shapesize(0.2, 0.2)
        spike.penup()
        spike.speed(0)
        spiky_ball.spikes = spiky_ball.spikes if hasattr(spiky_ball, 'spikes') else []
        spiky_ball.spikes.append(spike)
    spiky_ball.penup()
    spiky_ball.speed(0)
    size = random.uniform(0.5, 2)
    spiky_ball.shapesize(size, size)
    x = random.randint(-280, 280)
    y = 350
    spiky_ball.goto(x, y)
    spiky_ball.dy = random.uniform(1, 3)  # Kecepatan jatuh
    spiky_balls.append(spiky_ball)

# Fungsi untuk menggerakkan bola yang dikontrol
def move_left():
    x = player_ball.xcor()
    x -= 20
    if x < -280:
        x = -280
    player_ball.setx(x)

def move_right():
    x = player_ball.xcor()
    x += 20
    if x > 280:
        x = 280
    player_ball.setx(x)

# Pengaturan keyboard
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Loop utama animasi
while True:
    # Membuat bola berduri baru secara acak
    if random.randint(1, 30) == 1:  # Tingkat kemunculan
        create_spiky_ball()

    # Menggerakkan dan memeriksa tabrakan bola berduri
    for ball in spiky_balls:
        ball.sety(ball.ycor() - ball.dy)
        # Menggerakkan "duri" mengikuti bola utama
        if hasattr(ball, 'spikes'):
            size_factor = ball.shapesize()[0]
            for i, spike in enumerate(ball.spikes):
                angle = i * 45  # Sudut untuk setiap duri
                radius = 10 * size_factor
                spike_x = ball.xcor() + radius * turtle.math.cos(turtle.math.radians(angle))
                spike_y = ball.ycor() + radius * turtle.math.sin(turtle.math.radians(angle))
                spike.goto(spike_x, spike_y)

        # Deteksi tabrakan
        if player_ball.distance(ball) < 15 * ball.shapesize()[0]:
            print("Game Over!")
            screen.bye()

        # Menghapus bola yang keluar layar bawah
        if ball.ycor() < -350:
            ball.hideturtle()
            if hasattr(ball, 'spikes'):
                for spike in ball.spikes:
                    spike.hideturtle()
            spiky_balls.remove(ball)

    screen.update()

screen.mainloop()