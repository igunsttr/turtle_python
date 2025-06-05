# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 09:00:04 2025

@author: office
"""

from PIL import Image

def crop_image(input_path, output_path, left, upper, right, lower):
    """Memotong bagian gambar sesuai koordinat yang diberikan."""
    try:
        img = Image.open(input_path)
        # Koordinat crop: (left, upper, right, lower)
        cropped_img = img.crop((left, upper, right, lower))
        cropped_img.save(output_path)
        print(f"Gambar berhasil dipotong dan disimpan ke: {output_path}")
    except FileNotFoundError:
        print(f"Error: File tidak ditemukan di {input_path}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan:
# Misalnya, memotong bagian tengah gambar 300x300 dari gambar asli
crop_image('input.png', 'cropped_image.jpg', 300, 300, 50, 50)