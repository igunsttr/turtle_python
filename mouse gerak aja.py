# -*- coding: utf-8 -*-
"""
Created on Thu May 22 12:45:32 2025

@author: office
"""

import turtle
import random
import time

# --- Setup Layar Game ---
layar = turtle.Screen()
layar.setup(width=600, height=800) # Ukuran layar lebih tinggi untuk meteor jatuh
layar.tracer(0)  # Mematikan update otomatis untuk animasi yang lebih halus
layar.bgcolor("lightgreen")
layar.title("Penghindar Meteor!")

# --- Karakter Pemain ---
pemain = turtle.Turtle()
pemain.shape("square")
pemain.color("red")
pemain.shapesize(stretch_wid=1.5, stretch_len=1.5) # Ukuran pemain
pemain.penup()
pemain.goto(0, -350) # Posisi awal pemain di bagian bawah layar
pemain.speed(0)


# --- Fungsi Gerak Pemain dengan Mouse Click ---
def gerak_pemain_ke_klik(x, y):
    # Memastikan pemain tetap di bagian bawah layar
#    if y > -300: # Jika klik terlalu tinggi, pemain akan tetap di ketinggian ini
#        y_target = -300
#    else:
#        y_target = y

    pemain.goto(x, y) # Pindahkan pemain ke posisi klik X dan Y yang disesuaikan
    layar.update()
    
# --- Event Listener (Kontrol Pemain) ---
layar.listen()
layar.onclick(gerak_pemain_ke_klik) # Pemain bergerak saat mouse diklik

# --- Game Loop ---
game_aktif = True

while game_aktif:
    layar.update() # Perbarui layar setelah semua pergerakan
    time.sleep(1) # Sedikit jeda untuk mengontrol kecepatan game

# Menutup layar saat game berakhir
layar.mainloop()