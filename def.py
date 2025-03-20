# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 12:13:25 2025

@author: office
"""

import turtle

# Fungsi untuk menggambar persegi
def gambar_persegi(panjang):
  for _ in range(4):
    turtle.forward(panjang)
    turtle.left(90)

# Fungsi untuk menggambar segitiga
def gambar_segitiga(panjang):
  for _ in range(3):
    turtle.forward(panjang)
    turtle.left(120)

# Fungsi untuk menggambar lingkaran
def gambar_lingkaran(radius):
  turtle.circle(radius)

# Fungsi untuk menggambar bintang
def gambar_bintang(panjang):
  for _ in range(5):
    turtle.forward(panjang)
    turtle.right(144)

# Fungsi untuk menggambar bentuk kustom
def gambar_bentuk_kustom(panjang, sudut, jumlah_sisi):
    for _ in range(jumlah_sisi):
        turtle.forward(panjang)
        turtle.left(sudut)

# Contoh penggunaan fungsi-fungsi tersebut
turtle.speed(0)  # Atur kecepatan gambar (0 = tercepat)

gambar_persegi(100)
turtle.penup()
turtle.forward(150)
turtle.pendown()

gambar_segitiga(100)
turtle.penup()
turtle.forward(150)
turtle.pendown()

gambar_lingkaran(50)
turtle.penup()
turtle.forward(150)
turtle.pendown()

gambar_bintang(100)
turtle.penup()
turtle.forward(150)
turtle.pendown()

gambar_bentuk_kustom(100, 72, 5) # Menggambar pentagon

turtle.hideturtle()  # Sembunyikan kura-kura setelah selesai
turtle.done()
turtle.exitonclick()

