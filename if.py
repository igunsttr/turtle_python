# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 12:07:20 2025

@author: office
"""

import turtle
import random

# Membuat objek kura-kura
t = turtle.Turtle()

# Fungsi untuk menggambar bentuk acak
def gambar_bentuk():
    # Memilih warna acak
    warna = random.choice(["red", "blue", "green", "yellow"])
    t.color(warna)

    # Memilih bentuk acak
    bentuk = random.choice(["persegi", "lingkaran", "segitiga"])

    if bentuk == "persegi":
        for i in range(4):
            t.forward(100)
            t.left(90)
    elif bentuk == "lingkaran":
        t.circle(50)
    else:  # bentuk == "segitiga"
        for i in range(3):
            t.forward(100)
            t.left(120)

# Memanggil fungsi untuk menggambar bentuk
gambar_bentuk()

# Menutup jendela ketika diklik
turtle.exitonclick()