import turtle
import random
import time

# --- Setup Layar Game ---
layar = turtle.Screen()
layar.setup(width=600, height=800) # Ukuran layar lebih tinggi untuk meteor jatuh
layar.tracer(0)  # Mematikan update otomatis untuk animasi yang lebih halus
layar.bgcolor("darkblue")
layar.title("Penghindar Meteor!")

# --- Karakter Pemain ---
pemain = turtle.Turtle()
pemain.shape("square")
pemain.color("lime green")
pemain.shapesize(stretch_wid=1.5, stretch_len=1.5) # Ukuran pemain
pemain.penup()
pemain.goto(0, -350) # Posisi awal pemain di bagian bawah layar
pemain.speed(0)

# --- Daftar Meteor ---
meteor_list = []
jumlah_meteor_maks = 8 # Jumlah maksimum meteor di layar pada satu waktu
meteor_spawn_interval = 1.5 # Interval waktu untuk menciptakan meteor baru

# --- Fungsi Membuat Meteor Baru ---
def buat_meteor():
    meteor = turtle.Turtle()
    meteor.shape("circle")
    meteor.color("gray")
    meteor.shapesize(stretch_wid=0.7, stretch_len=0.7)
    meteor.penup()
    # Posisi X acak di bagian atas layar
    meteor.goto(random.randint(-280, 280), 380)
    # Kecepatan jatuh meteor acak (antara 2 hingga 8)
    meteor.fall_speed = random.uniform(2, 8)
    meteor_list.append(meteor)

# --- Fungsi Gerak Pemain dengan Mouse Click ---
def gerak_pemain_ke_klik(x, y):
    # Memastikan pemain tetap di bagian bawah layar
    if y > -300: # Jika klik terlalu tinggi, pemain akan tetap di ketinggian ini
        y_target = -300
    else:
        y_target = y

    pemain.goto(x, y_target) # Pindahkan pemain ke posisi klik X dan Y yang disesuaikan
    layar.update()

# --- Skor ---
skor = 0
penulis_skor = turtle.Turtle()
penulis_skor.penup()
penulis_skor.hideturtle()
penulis_skor.goto(0, 350)
penulis_skor.color("white")
penulis_skor.write(f"Skor: {skor}", align="center", font=("Arial", 24, "normal"))

# --- Fungsi Deteksi Kolisi ---
def is_collision(obj1, obj2):
    # Menggunakan jarak antara pusat kedua objek
    jarak = obj1.distance(obj2)
    # Sesuaikan nilai ini berdasarkan ukuran objekmu
    if jarak < 25: # Jarak tabrakan yang dianggap kolisi
        return True
    return False

# --- Event Listener (Kontrol Pemain) ---
layar.listen()
layar.onclick(gerak_pemain_ke_klik) # Pemain bergerak saat mouse diklik

# --- Game Loop ---
game_aktif = True
last_meteor_spawn_time = time.time()

while game_aktif:
    current_time = time.time()

    # Membuat meteor baru jika belum mencapai batas dan sudah waktunya
    if len(meteor_list) < jumlah_meteor_maks and \
       (current_time - last_meteor_spawn_time) > meteor_spawn_interval:
        buat_meteor()
        last_meteor_spawn_time = current_time
        # Membuat game lebih menantang: meteor_spawn_interval berkurang seiring waktu
        if meteor_spawn_interval > 0.5:
            meteor_spawn_interval -= 0.05 # Meteor akan lebih sering muncul

    # Pergerakan dan Penanganan Meteor
    meteors_to_remove = [] # Daftar meteor yang akan dihapus setelah iterasi
    for meteor in meteor_list:
        meteor.sety(meteor.ycor() - meteor.fall_speed)

        # Jika meteor keluar dari bawah layar, tandai untuk dihapus dan tambah skor
        if meteor.ycor() < -400:
            meteor.clear()
            meteor.hideturtle()
            meteors_to_remove.append(meteor)
            skor += 1
            penulis_skor.clear()
            penulis_skor.write(f"Skor: {skor}", align="center", font=("Arial", 24, "normal"))

        # Deteksi Kolisi dengan Pemain
        if is_collision(pemain, meteor):
            game_aktif = False # Game Over
            penulis_skor.clear()
            penulis_skor.goto(0, 0)
            penulis_skor.color("red")
            penulis_skor.write(f"GAME OVER!\nSkor Akhir: {skor}", align="center", font=("Arial", 36, "bold"))
            break # Keluar dari loop meteor jika game over

    # Hapus meteor yang sudah keluar layar
    for meteor in meteors_to_remove:
        if meteor in meteor_list: # Pastikan meteor masih ada di list
            meteor_list.remove(meteor)

    layar.update() # Perbarui layar setelah semua pergerakan
    time.sleep(0.01) # Sedikit jeda untuk mengontrol kecepatan game

# Menutup layar saat game berakhir
layar.mainloop()