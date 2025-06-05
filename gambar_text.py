# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 08:55:11 2025

@author: office
"""

from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(input_path, output_path, text, position, font_path=None, font_size=30, text_color=(0, 0, 0)):
    """Menambahkan teks pada gambar."""
    try:
        img = Image.open(input_path)
        draw = ImageDraw.Draw(img)

        # Muat font kustom jika disediakan, jika tidak gunakan default Pillow
        if font_path:
            try:
                font = ImageFont.truetype(font_path, font_size)
            except IOError:
                print(f"Peringatan: Font tidak ditemukan di {font_path}. Menggunakan font default.")
                font = ImageFont.load_default()
        else:
            font = ImageFont.load_default()

        draw.text(position, text, fill=text_color, font=font)
        img.save(output_path)
        print(f"Teks berhasil ditambahkan dan gambar disimpan ke: {output_path}")
    except FileNotFoundError:
        print(f"Error: File tidak ditemukan di {input_path}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan:
# Untuk menggunakan font kustom, Anda perlu file .ttf atau .otf.
# Misalnya, Anda bisa mengunduh font dari Google Fonts dan menyimpannya di folder yang sama.
# font_file = 'arial.ttf' # Ganti dengan path ke font Anda
#add_text_to_image('input.jpg', 'image_with_text.jpg', "Halo Dunia!", (10, 10), font_path=font_file, font_size=40, text_color=(255, 0, 0)) 
add_text_to_image('input.png', 'gambar_text.jpg', "Informatika", (200, 200), font_size=30, text_color=(249, 0, 255))