import turtle
t = turtle.Turtle()

# Loop untuk menggambar bentuk
for i in range(10):
    # Kondisi untuk mengubah warna
    if i % 2 == 0:
        t.color("red")
    else:
        t.color("blue")

    # Menggambar garis
    t.forward(50)
    t.left(36)

# Menyembunyikan Turtle
t.hideturtle()

# Menutup jendela Turtle saat diklik
turtle.done()
turtle.exitonclick()