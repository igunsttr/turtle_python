# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 12:45:49 2025

@author: office
"""


import turtle

# Inisialisasi layar
layar = turtle.Screen()
layar.setup(600, 600)
layar.title("Game Sederhana dengan Turtle")

# Inisialisasi pemain
pemain = turtle.Turtle()
pemain.shape("circle")
pemain.color("blue")
pemain.penup()
pemain.goto(0, -250)

# Fungsi untuk menggerakkan pemain ke posisi mouse
def gerak_pemain(x, y):
  pemain.goto(x, -250)

# Mendeteksi klik mouse
layar.onclick(gerak_pemain)

# Game loop
while True:
  layar.update()