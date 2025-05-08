# -*- coding: utf-8 -*-
"""
Created on Thu May  8 09:32:53 2025

@author: office
"""

import turtle

# Inisialisasi layar
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("lightgreen")
screen.tracer(0)  # Menonaktifkan update layar otomatis

# Membuat bola
bola = turtle.Turtle()
bola.shape("circle")
bola.color("red")
bola.penup()
bola.goto(0, 0)
bola.speed(0)

# Kecepatan gerakan
kecepatan = 20

# Fungsi untuk menggerakkan bola ke atas
def gerak_atas():
    y = bola.ycor()
    bola.sety(y + kecepatan)

# Fungsi untuk menggerakkan bola ke bawah
def gerak_bawah():
    y = bola.ycor()
    bola.sety(y - kecepatan)

# Fungsi untuk menggerakkan bola ke kiri
def gerak_kiri():
    x = bola.xcor()
    bola.setx(x - kecepatan)

# Fungsi untuk menggerakkan bola ke kanan
def gerak_kanan():
    x = bola.xcor()
    bola.setx(x + kecepatan)

# Mengikat tombol keyboard dengan fungsi gerakan
screen.listen()
screen.onkeypress(gerak_atas, "Up")
screen.onkeypress(gerak_bawah, "Down")
screen.onkeypress(gerak_kiri, "Left")
screen.onkeypress(gerak_kanan, "Right")

# Loop utama animasi
while True:
    screen.update()

    # Batasan layar agar bola tidak keluar
    if bola.xcor() > 290:
        bola.setx(290)
    elif bola.xcor() < -290:
        bola.setx(-290)
    elif bola.ycor() > 290:
        bola.sety(290)
    elif bola.ycor() < -290:
        bola.sety(-290)

screen.mainloop()