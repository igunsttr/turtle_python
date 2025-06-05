# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 08:54:20 2025

@author: office
"""

from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
    """Mengubah ukuran gambar ke dimensi yang ditentukan."""
    try:
        img = Image.open(input_path)
        resized_img = img.resize((new_width, new_height))
        resized_img.save(output_path)
        print(f"Gambar berhasil diubah ukurannya dan disimpan ke: {output_path}")
    except FileNotFoundError:
        print(f"Error: File tidak ditemukan di {input_path}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan:
resize_image('input.png', 'resized_jpg.jpg', 1000, 1000)