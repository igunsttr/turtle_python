
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
# Animasi utama
def animate():
    for i in range(200):
        t.circle(100)  # Membuat lingkaran dengan radius 100
        t.left(10)     # Berputar 10 derajat setiap langkah
        randomize()     # Mengubah warna dan ukuran secara acak        
    t.clear()           # Membersihkan layar setelah selesai
    animate()           # Mengulang animasi

# Memulai animasi
animate()
# Menjaga window tetap terbuka
t.done()