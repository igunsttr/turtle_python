import turtle
import random
import time

# --- Setup Layar Game ---
layar = turtle.Screen()
layar.setup(width=800, height=400)
layar.tracer(0)  # Mematikan update otomatis
layar.bgcolor("lightblue")
layar.title("Game Lompat Sederhana")

# --- Karakter Utama ---
karakter = turtle.Turtle()
karakter.shape("square")
karakter.color("blue")
karakter.shapesize(stretch_wid=2, stretch_len=1)
karakter.penup()
karakter.goto(-300, -100)
karakter.speed(0)

is_jumping = False
jump_height = 0
gravity = 0.8 # Nilai gravitasi
jump_speed = 15 # Kecepatan lompat awal

# --- Halangan ---
halangan_list = []
jumlah_halangan = 1

for _ in range(jumlah_halangan):
    halangan = turtle.Turtle()
    halangan.shape("square")
    halangan.color("red")
    halangan.shapesize(stretch_wid=2, stretch_len=1)
    halangan.penup()
    halangan.speed(0)
    halangan.goto(random.randint(400, 800), -100) # Posisi awal halangan acak
    halangan_list.append(halangan)

halangan_speed = 1 # Kecepatan gerakan halangan

# --- Skor ---
skor = 0
penulis_skor = turtle.Turtle()
penulis_skor.penup()
penulis_skor.hideturtle()
penulis_skor.goto(300, 150)
penulis_skor.color("black")
penulis_skor.write(f"Skor: {skor}", align="center", font=("Arial", 20, "normal"))

# --- Fungsi Lompat ---
def lompat():
    global is_jumping, jump_height
    if not is_jumping:
        is_jumping = True
        jump_height = jump_speed # Set kecepatan lompat awal

# --- Fungsi Deteksi Kolisi ---
def is_collision(t1, t2):
    jarak = t1.distance(t2)
    # Sesuaikan nilai ini berdasarkan ukuran karakter dan halangan Anda
    if jarak < 30:
        return True
    return False

# --- Event Listener (Spasi untuk Lompat) ---
layar.listen()
layar.onkeypress(lompat, "space")

# --- Game Loop ---
game_aktif = True
while game_aktif:
    layar.update()
    time.sleep(0.01) # Mengurangi penggunaan CPU, membuat animasi lebih halus

    # Pergerakan Lompat
    if is_jumping:
        karakter.sety(karakter.ycor() + jump_height)
        jump_height -= gravity # Mengurangi tinggi lompatan karena gravitasi
        if karakter.ycor() <= -100: # Jika karakter kembali ke tanah
            karakter.sety(-100)
            is_jumping = False
            jump_height = 0

    # Pergerakan Halangan
    for halangan in halangan_list:
        halangan.setx(halangan.xcor() - halangan_speed)

        # Jika halangan keluar layar, reset posisinya dan tambah skor
        if halangan.xcor() < -400:
            halangan.goto(random.randint(400, 800), -100)
            skor += 1
            penulis_skor.clear()
            penulis_skor.write(f"Skor: {skor}", align="center", font=("Arial", 20, "normal"))

        # Deteksi Kolisi
        if is_collision(karakter, halangan):
            game_aktif = False # Game Over
            penulis_skor.goto(0, 0)
            penulis_skor.color("red")
            penulis_skor.write("GAME OVER!", align="center", font=("Arial", 30, "bold"))

# Menutup layar saat game berakhir
layar.mainloop()