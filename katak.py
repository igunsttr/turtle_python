# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 12:28:15 2025

@author: office
"""

import turtle
import random

# Inisialisasi layar
layar = turtle.Screen()
layar.bgcolor("lightblue")
layar.title("Tangkap Kotak!")

# Inisialisasi kotak
kotak = turtle.Turtle()
kotak.shape("square")
kotak.color("red")
kotak.penup()
kotak.goto(random.randint(-200, 200), random.randint(-200, 200))

# Inisialisasi pemain
pemain = turtle.Turtle()
pemain.shape("turtle")
pemain.color("green")
pemain.penup()

# Fungsi untuk menggerakkan pemain
def gerak_maju():
  pemain.forward(10)

def gerak_kiri():
  pemain.left(45)

def gerak_kanan():
  pemain.right(45)

# Menetapkan pendengar tombol
layar.listen()
layar.onkey(gerak_maju, "Up")
layar.onkey(gerak_kiri, "Left")
layar.onkey(gerak_kanan, "Right")

# Game loop
while True:
  # Cek tabrakan
  if pemain.distance(kotak) < 20:
    kotak.goto(random.randint(-200, 200), random.randint(-200, 200))

turtle.done()