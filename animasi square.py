# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 08:19:27 2025

@author: office
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 07:55:41 2025

@author: office
"""

import turtle
import random

# Setup layar
screen = turtle.Screen()
screen.title("Animasi Turtle Sederhana")
screen.bgcolor("black")
screen.setup(width=600, height=600)
# Membuat turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)

# Daftar warna
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
# Fungsi untuk mengubah warna dan ukuran secara acak
def randomize():
    t.color(random.choice(colors))
    t.pensize(random.randint(1, 5))
def animate():
    size = 10
    for i in range(100):
        t.forward(size)
        t.left(90)
        size += 5
        randomize()
    t.clear()
    animate()  
# Memulai animasi
animate()
# Menjaga window tetap terbuka
t.done()