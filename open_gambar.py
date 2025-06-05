# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 08:50:39 2025

@author: office
"""

from PIL import Image

def open_and_save_image(input_path, output_path):
    """Membuka gambar dan menyimpannya ke lokasi baru."""
    try:
        img = Image.open(input_path)
        print(f"Gambar berhasil dibuka: {input_path}")
        img.save(output_path)
        print(f"Gambar berhasil disimpan: {output_path}")
    except FileNotFoundError:
        print(f"Error: File tidak ditemukan di {input_path}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh penggunaan:
# Pastikan Anda memiliki gambar dengan nama 'input.jpg' di direktori yang sama
# atau berikan path lengkap ke gambar Anda.
open_and_save_image('input.png', 'output.jpg')