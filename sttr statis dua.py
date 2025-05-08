# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 09:13:28 2025

@author: office
"""

import turtle
import random
import time

# Setup layar
screen = turtle.Screen()
screen.title("UTR CEPU - Jurusan Informatika")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Mematikan update otomatis

# Membuat turtle untuk text utama
text_utama = turtle.Turtle()
text_utama.hideturtle()
text_utama.penup()
text_utama.goto(0, 50)  # Posisi lebih atas

# Membuat turtle untuk subtext
sub_text = turtle.Turtle()
sub_text.hideturtle()
sub_text.penup()
sub_text.goto(0, -50)  # Posisi lebih bawah

# Membuat turtle untuk subtext
sub_text2 = turtle.Turtle()
sub_text2.hideturtle()
sub_text2.penup()
sub_text2.goto(0, -100)  # Posisi lebih bawah

def random_color():
    """Menghasilkan warna RGB acak"""
    return (random.random(), random.random(), random.random())

def update_text():
    while True:
        # Generate warna baru
        color1 = random_color()
        color2 = random_color()
        color3= random_color()
        # Hapus text lama
        text_utama.clear()
        sub_text.clear()
        
        # Gambar text baru dengan warna acak
        text_utama.color(color1)
        text_utama.write("UTR CEPU", 
                       align="center", 
                       font=("Arial", 48, "bold"))
        
        sub_text.color(color2)
        sub_text.write("Jurusan Informatika", 
                      align="center", 
                      font=("Arial", 24, "normal"))
        
        sub_text2.color(color3)
        sub_text2.write("Jl.Kampus Ronggolawe, Cepu, Jawa tengah", 
                      align="center", 
                      font=("Arial", 18, "normal"))
        # Update layar
        screen.update()
        
        # Jeda waktu
        time.sleep(0.5)

# Jalankan animasi
update_text()
turtle.done()