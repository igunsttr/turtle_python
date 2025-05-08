# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 08:26:26 2025

@author: office
"""

import turtle
import time

# Setup layar
screen = turtle.Screen()
screen.title("Animasi Tulisan STTR CEPU")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Mematikan update otomatis untuk animasi lebih smooth

# Membuat turtle untuk text
text = turtle.Turtle()
text.hideturtle()
text.speed(0)
text.penup()

# Variabel animasi
dx = 3  # Kecepatan horizontal
dy = 2  # Kecepatan vertikal
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
color_index = 0

def animate():
    global dx, dy, color_index
    while True:
        text.clear()  # Hapus text sebelumnya
        
        # Update posisi
        x = text.xcor() + dx
        y = text.ycor() + dy
        
        # Cek batas layar dan pantulkan
        if x > 350 or x < -350:
            dx *= -1  # Balik arah horizontal
        if y > 250 or y < -250:
            dy *= -1  # Balik arah vertikal
        
        # Update warna setiap 5 frame
        if color_index >= len(colors):
            color_index = 0
        text.color(colors[color_index])
        
        # Tampilkan text
        text.goto(x, y)
        text.write("STTR CEPU", align="center", font=("Arial", 40, "bold"))
        
        # Update layar
        screen.update()
        time.sleep(0.01)
        
        # Increment warna setiap 5 frame
        if int(text.xcor()) % 5 == 0:
            color_index += 1

# Jalankan animasi
animate()
turtle.done()