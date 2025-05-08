# -*- coding: utf-8 -*-
"""
Created on Thu May  8 09:37:01 2025

@author: office
"""

import turtle
import random
import time

# Inisialisasi layar
layar = turtle.Screen()
layar.setup(width=600, height=600)
layar.bgcolor("lightblue")
layar.tracer(0)  # Menonaktifkan update layar otomatis

# Bola pemain
bola = turtle.Turtle()
bola.shape("circle")
bola.color("red")
bola.penup()
bola.speed(0)
bola.goto(0, -250)
bola.arah = "stop"

# Skor
skor = 0
nyawa = 3
pena_skor = turtle.Turtle()
pena_skor.speed(0)
pena_skor.color("black")
pena_skor.penup()
pena_skor.hideturtle()
pena_skor.goto(0, 260)
pena_skor.write(f"Skor: {skor}  Nyawa: {nyawa}", align="center", font=("Courier New", 24, "normal"))

# Daftar bola duri
bola_duri_list = []
jumlah_bola_duri = 10

for _ in range(jumlah_bola_duri):
    bola_duri = turtle.Turtle()
    bola_duri.shape("circle")
    bola_duri.color("gray")
    bola_duri.penup()
    bola_duri.speed(0)
    ukuran = random.uniform(0.5, 2)
    bola_duri.shapesize(stretch_wid=ukuran, stretch_len=ukuran)
    x_acak = random.randint(-280, 280)
    y_acak = random.randint(300, 500)
    bola_duri.goto(x_acak, y_acak)
    bola_duri.kecepatan = random.randint(1, 4)
    bola_duri_list.append(bola_duri)

# Daftar bonus
bonus_list = []
jumlah_bonus = 5

for _ in range(jumlah_bonus):
    bonus = turtle.Turtle()
    bonus.shape("square")
    bonus.color("green")
    bonus.penup()
    bonus.speed(0)
    ukuran = random.uniform(0.5, 1.5)
    bonus.shapesize(stretch_wid=ukuran, stretch_len=ukuran)
    x_acak = random.randint(-280, 280)
    y_acak = random.randint(300, 500)
    bonus.goto(x_acak, y_acak)
    bonus.kecepatan = random.randint(1, 3)
    bonus_list.append(bonus)

# Fungsi untuk menggerakkan bola pemain
def gerak_kiri():
    bola.arah = "kiri"

def gerak_kanan():
    bola.arah = "kanan"

def set_stop():
    bola.arah = "stop"

def gerakkan_bola_pemain():
    if bola.arah == "kiri":
        x = bola.xcor()
        x -= 20
        bola.setx(x)
    if bola.arah == "kanan":
        x = bola.xcor()
        x += 20
        bola.setx(x)

    # Batasan layar untuk bola pemain
    if bola.xcor() < -290:
        bola.setx(-290)
        bola.arah = "stop"
    if bola.xcor() > 290:
        bola.setx(290)
        bola.arah = "stop"

# Binding keyboard
layar.listen()
layar.onkeypress(gerak_kiri, "Left")
layar.onkeypress(gerak_kanan, "Right")
layar.onkeyrelease(set_stop, "Left")
layar.onkeyrelease(set_stop, "Right")

# Loop utama game
while True:
    layar.update()

    gerakkan_bola_pemain()

    # Gerakkan bola duri
    for bola_duri in bola_duri_list:
        y = bola_duri.ycor()
        y -= bola_duri.kecepatan
        bola_duri.sety(y)

        # Reset bola duri jika keluar layar
        if y < -300:
            x_acak = random.randint(-280, 280)
            y_acak = random.randint(300, 500)
            ukuran = random.uniform(0.5, 2)
            bola_duri.shapesize(stretch_wid=ukuran, stretch_len=ukuran)
            bola_duri.goto(x_acak, y_acak)
            bola_duri.kecepatan = random.randint(1, 4)

        # Deteksi tabrakan dengan bola pemain
        if bola.distance(bola_duri) < 20 * bola_duri.shapesize()[0]:
            nyawa -= 1
            pena_skor.clear()
            pena_skor.write(f"Skor: {skor}  Nyawa: {nyawa}", align="center", font=("Courier New", 24, "normal"))
            x_acak = random.randint(-280, 280)
            y_acak = random.randint(300, 500)
            ukuran = random.uniform(0.5, 2)
            bola_duri.shapesize(stretch_wid=ukuran, stretch_len=ukuran)
            bola_duri.goto(x_acak, y_acak)
            bola_duri.kecepatan = random.randint(1, 4)

            if nyawa == 0:
                pena_skor.clear()
                pena_skor.write("Game Over!", align="center", font=("Courier New", 36, "bold"))
                time.sleep(2)
                layar.bye()

    # Gerakkan bonus
    for bonus in bonus_list:
        y = bonus.ycor()
        y -= bonus.kecepatan
        bonus.sety(y)

        # Reset bonus jika keluar layar
        if y < -300:
            x_acak = random.randint(-280, 280)
            y_acak = random.randint(300, 500)
            ukuran = random.uniform(0.5, 1.5)
            bonus.shapesize(stretch_wid=ukuran, stretch_len=ukuran)
            bonus.goto(x_acak, y_acak)
            bonus.kecepatan = random.randint(1, 3)

        # Deteksi tabrakan dengan bola pemain (bonus)
        if bola.distance(bonus) < 20 * bonus.shapesize()[0]:
            skor += 10
            pena_skor.clear()
            pena_skor.write(f"Skor: {skor}  Nyawa: {nyawa}", align="center", font=("Courier New", 24, "normal"))
            x_acak = random.randint(-280, 280)
            y_acak = random.randint(300, 500)
            ukuran = random.uniform(0.5, 1.5)
            bonus.shapesize(stretch_wid=ukuran, stretch_len=ukuran)
            bonus.goto(x_acak, y_acak)
            bonus.kecepatan = random.randint(1, 3)

    time.sleep(0.01)

layar.mainloop()