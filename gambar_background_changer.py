from PIL import Image

def ubah_warna_tertentu(input_path, output_path, warna_lama_rgb, warna_baru_rgb, toleransi=10):
    """
    Mengubah warna tertentu dalam gambar menjadi warna lain.

    Args:
        input_path (str): Path ke gambar input.
        output_path (str): Path untuk menyimpan gambar output.
        warna_lama_rgb (tuple): Tuple RGB dari warna yang ingin diubah (contoh: (255, 0, 0) untuk merah).
        warna_baru_rgb (tuple): Tuple RGB dari warna pengganti (contoh: (0, 0, 255) untuk biru).
        toleransi (int, optional): Toleransi untuk mencocokkan warna (0-255).
                                   Piksel yang warnanya mendekati warna_lama dalam batas toleransi
                                   akan diubah. Default adalah 10.
                                   Nilai yang lebih besar berarti lebih banyak variasi warna yang akan diubah.
    """
    try:
        # Buka gambar dan konversi ke mode RGB untuk konsistensi
        # Ini penting agar kita selalu berurusan dengan 3 channel (R, G, B)
        img = Image.open(input_path).convert('RGB')
        pixels = img.load() # Memuat piksel untuk akses cepat dan modifikasi

        lebar, tinggi = img.size

        # Menghitung toleransi maksimum gabungan untuk semua channel (R+G+B)
        # toleransi_total akan menjadi 3 * toleransi_per_channel
        toleransi_total = toleransi * 3

        for x in range(lebar):
            for y in range(tinggi):
                r, g, b = pixels[x, y] # Dapatkan nilai RGB piksel saat ini

                # Hitung perbedaan absolut antara warna piksel saat ini dan warna_lama_rgb
                # Ini adalah "Manhattan distance" atau L1 norm
                diff_r = abs(r - warna_lama_rgb[0])
                diff_g = abs(g - warna_lama_rgb[1])
                diff_b = abs(b - warna_lama_rgb[2])

                total_diff = diff_r + diff_g + diff_b

                # Jika total perbedaan kurang dari atau sama dengan toleransi_total,
                # berarti piksel ini cukup dekat dengan warna yang ingin diubah
                if total_diff <= toleransi_total:
                    pixels[x, y] = warna_baru_rgb # Ubah warna piksel

        img.save(output_path)
        print(f"Warna berhasil diubah dan gambar disimpan ke: {output_path}")

    except FileNotFoundError:
        print(f"Error: File tidak ditemukan di {input_path}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# --- Contoh Penggunaan ---
# Pastikan Anda memiliki gambar untuk diuji, misalnya 'contoh_gambar.jpg'
# Anda bisa menggunakan gambar apa pun yang memiliki area dengan warna yang ingin Anda ubah.

# Contoh 1: Mengubah semua piksel yang mendekati merah menjadi biru
# Misalnya, jika Anda punya gambar dengan elemen merah dan Anda ingin mengubahnya menjadi biru.
# ubah_warna_tertentu('contoh_gambar.jpg', 'gambar_merah_ke_biru.jpg', (255, 0, 0), (0, 0, 255), toleransi=20)

# Contoh 2: Mengubah area putih menjadi hitam
# Jika Anda punya gambar dengan background putih atau objek putih, dan ingin mengubahnya menjadi hitam.
# ubah_warna_tertentu('contoh_gambar.jpg', 'gambar_putih_ke_hitam.png', (255, 255, 255), (0, 0, 0), toleransi=15)

# Contoh 3: Mengubah warna putih menjadi kuning hijau
ubah_warna_tertentu('input.png', 'input_background.jpg', (255, 255, 255), (5, 100, 100), toleransi=30)