# Aplikasi Monitoring Website Asinkron

## Deskripsi
Project ini adalah aplikasi Python untuk memonitor status HTTP dari beberapa website secara "asinkron" menggunakan modul `asyncio` dan `aiohttp`.

Aplikasi ini akan:
- Mengecek status HTTP dari minimal 5 situs setiap 10 detik.
- Memberikan peringatan jika status situs bukan 200 (SITE DOWN!).
- Menyimpan hasil pengecekan ke file `log.txt`.
- Berjalan terus menerus (infinite loop).

## Fitur Bonus
- Mengeluarkan bunyi notifikasi (`\a`) jika ada situs yang down.
- Struktur kode lebih modular dengan fungsi `log_to_file()` terpisah.

## Cara Menjalankan
1. Pastikan sudah menginstal `aiohttp`:
    ```bash
    pip install aiohttp
    ```

2. Jalankan program:
    ```bash
    python monitor.py
    ```

3. Program akan berjalan terus menerus dan mengecek status situs setiap 10 detik.

## Struktur File
- `monitor.py` : Program utama untuk monitoring website.
- `log.txt` : File log yang mencatat hasil pengecekan.

## Catatan
Jika ingin menambahkan atau mengganti daftar website yang dipantau, ubah daftar `websites` di dalam file `monitor.py`.

## Author
- Nama : [Aji Nur Fahrurrahman]
- NIM : [122203004]
- Universitas Paramadina
