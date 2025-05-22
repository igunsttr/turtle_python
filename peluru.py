# -*- coding: utf-8 -*-
"""
Created on Thu May 22 12:22:48 2025

@author: office
"""

import turtle
import random
import time

# --- Setup Layar Game ---
layar = turtle.Screen()
layar.setup(width=600, height=800) # Ukuran layar lebih tinggi untuk jatuh peluru
layar.tracer(0)  # Mematikan update otomatis untuk animasi yang lebih halus
layar.bgcolor("lightgray")
layar.title("Hindari Peluru!")

# --- Karakter Pemain ---
pemain = turtle.Turtle()
pemain.shape("square")
pemain.color("blue")
pemain.shapesize(stretch_wid=1, stretch_len=3) # Bentuk persegi panjang horizontal
pemain.penup()
pemain.goto(0, -350) # Posisi pemain di bagian bawah layar
pemain.speed(0)

pemain_speed = 20 # Kecepatan gerak pemain

# --- Daftar Peluru ---
peluru_list = []
jumlah_peluru_maks = 5 # Jumlah maksimum peluru di layar
peluru_spawn_interval = 1.0 # Interval waktu untuk menciptakan peluru baru
last_spawn_time = time.time()

# --- Fungsi Membuat Peluru Baru ---
def buat_peluru():
    peluru = turtle.Turtle()
    peluru.shape("circle")
    peluru.color("red")
    peluru.shapesize(stretch_wid=0.8, stretch_len=0.8)
    peluru.penup()
    # Posisi X acak di bagian atas layar
    peluru.goto(random.randint(-280, 280), 380)
    peluru.speed(0)
    # Kecepatan jatuh peluru acak (antara 3 hingga 10)
    peluru.fall_speed = random.uniform(1, 3)
    peluru_list.append(peluru)

# --- Fungsi Gerak Pemain ---
def gerak_kiri():
    x = pemain.xcor()
    x -= pemain_speed
    if x < -280: # Batas kiri layar
        x = -280
    pemain.setx(x)

def gerak_kanan():
    x = pemain.xcor()
    x += pemain_speed
    if x > 280: # Batas kanan layar
        x = 280
    pemain.setx(x)

# --- Skor ---
skor = 0
penulis_skor = turtle.Turtle()
penulis_skor.penup()
penulis_skor.hideturtle()
penulis_skor.goto(0, 350)
penulis_skor.color("black")
penulis_skor.write(f"Skor: {skor}", align="center", font=("Arial", 24, "normal"))

# --- Fungsi Deteksi Kolisi ---
def is_collision(obj1, obj2):
    jarak = obj1.distance(obj2)
    # Sesuaikan nilai ini berdasarkan ukuran objekmu
    if jarak < 25: # Jarak tabrakan antara pemain dan peluru
        return True
    return False

# --- Event Listener (Kontrol Pemain) ---
layar.listen()
layar.onkeypress(gerak_kiri, "Left") # Panah kiri
layar.onkeypress(gerak_kanan, "Right") # Panah kanan

# --- Game Loop ---
game_aktif = True
while game_aktif:
    layar.update()
    current_time = time.time()

    # Membuat peluru baru jika belum mencapai batas dan sudah waktunya
    if len(peluru_list) < jumlah_peluru_maks and (current_time - last_spawn_time) > peluru_spawn_interval:
        buat_peluru()
        last_spawn_time = current_time
        # Sesuaikan interval spawn agar semakin cepat seiring waktu
        if peluru_spawn_interval > 0.3:
            peluru_spawn_interval -= 0.05 # Peluru akan lebih sering muncul

    # Pergerakan dan Penanganan Peluru
    for peluru in list(peluru_list): # Gunakan list() untuk menghindari masalah saat menghapus elemen
        peluru.sety(peluru.ycor() - peluru.fall_speed)

        # Jika peluru keluar dari bawah layar, hapus dan tambah skor
        if peluru.ycor() < -400:
            peluru.clear() # Hapus jejak peluru
            peluru.hideturtle()
            peluru_list.remove(peluru)
            skor += 1
            penulis_skor.clear()
            penulis_skor.write(f"Skor: {skor}", align="center", font=("Arial", 24, "normal"))

        # Deteksi Kolisi dengan Pemain
        if is_collision(pemain, peluru):
            game_aktif = False # Game Over
            penulis_skor.clear()
            penulis_skor.goto(0, 0)
            penulis_skor.color("red")
            penulis_skor.write(f"GAME OVER!\nSkor Akhir: {skor}", align="center", font=("Arial", 36, "bold"))
            break # Keluar dari loop peluru jika game over

# Menutup layar saat game berakhir
layar.mainloop()