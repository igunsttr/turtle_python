# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 09:08:36 2025

@author: office
"""

import turtle
import time

# Setup layar
screen = turtle.Screen()
screen.title("UTR CEPU - Animasi Warna")
screen.bgcolor("black")
screen.setup(width=800, height=400)
screen.tracer(0)  # Mematikan update otomatis

# Membuat turtle untuk text
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, 0)  # Posisi tengah

# Daftar warna untuk animasi
colors = [
    "#FF0000", "#FF4500", "#FFFF00",  # Merah, Oranye, Kuning
    "#00FF00", "#00FFFF", "#0000FF",  # Hijau, Cyan, Biru
    "#8A2BE2", "#FF00FF"              # Ungu, Magenta
]

def animate_color():
    color_index = 0
    while True:
        # Update warna
        text.clear()
        text.color(colors[color_index % len(colors)])
        
        # Gambar ulang text dengan warna baru
        text.write("UTR CEPU", 
                  align="center", 
                  font=("Arial", 48, "bold"))
        
        # Update layar
        screen.update()
        
        # Ubah warna berikutnya
        color_index += 1
        
        # Kontrol kecepatan perubahan warna
        time.sleep(0.2)

# Jalankan animasi
animate_color()
turtle.done()