# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 12:21:46 2025

@author: office
"""

import turtle
import random

# Inisialisasi layar
layar = turtle.Screen()
layar.bgcolor("lightblue")

# Inisialisasi pemain
pemain = turtle.Turtle()
pemain.shape("turtle")
pemain.color("green")
pemain.penup()
pemain.goto(0, -200)

# Inisialisasi target
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.goto(random.randint(-200, 200), 200)

# Fungsi untuk menggerakkan pemain
def gerak_kiri():
    pemain.left(30)

def gerak_kanan():
    pemain.right(30)

# Fungsi untuk memeriksa tabrakan
def tabrakan():
    if pemain.distance(target) < 20:
        target.goto(random.randint(-200, 200), 200)

# Pengaturan kontrol
layar.listen()
layar.onkey(gerak_kiri, "Left")
layar.onkey(gerak_kanan, "Right")

# Loop utama
while True:
    pemain.forward(10)
    tabrakan()

turtle.done()
