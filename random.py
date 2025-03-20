# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 12:19:22 2025

@author: office
"""
import turtle
import random
# Inisialisasi turtle
t = turtle.Turtle()
t.speed(0)  # Kecepatan gambar tercepat

# Fungsi untuk menggambar benda tak beraturan
def gambar_benda_acak(jumlah_sisi, panjang_maks, sudut_maks):
  for _ in range(jumlah_sisi):
    panjang = random.randint(10, panjang_maks)
    sudut = random.randint(1, sudut_maks)
    t.forward(panjang)
    t.left(sudut)

# Contoh penggunaan
jumlah_sisi = 20  # Jumlah sisi benda
panjang_maks = 100  # Panjang maksimum sisi
sudut_maks = 170  # Sudut maksimum belokan

gambar_benda_acak(jumlah_sisi, panjang_maks, sudut_maks)

turtle.done()
turtle.exitonclick()