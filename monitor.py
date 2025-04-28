"Nama: Aji Nur Fahrurrahman"
"NIM: 122203004"
"Mata Kuliah: Pemrograman Asinkron"
"Tugas: Pertemuan 7 - UTS"

import asyncio
import aiohttp
from datetime import datetime

# Daftar situs yang akan dicek
URLS = [
    "https://openai.com",
    "https://google.com",
    "https://somewebsite.com",
    "https://example.com",
    "https://github.com"
]

LOG_FILE = "log.txt"

# Fungsi untuk mencatat log ke file
def log_to_file(message: str):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

# Fungsi untuk mengecek status situs
async def check_site(session, url):
    try:
        async with session.get(url) as response:
            status = response.status
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"[{timestamp}] {url} - Status: {status}"
            if status != 200:
                message += "      SITE DOWN!"
                print('\a')  # Notifikasi bunyi jika situs down
            print(message)
            log_to_file(message)
    except Exception as e:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"[{timestamp}] {url} - ERROR: {str(e)}      SITE DOWN!"
        print('\a')  # Notifikasi bunyi jika error
        print(error_message)
        log_to_file(error_message)

# Fungsi utama
async def monitor_sites():
    async with aiohttp.ClientSession() as session:
        while True:
            tasks = [check_site(session, url) for url in URLS]
            await asyncio.gather(*tasks)
            await asyncio.sleep(10)  # Tunggu 10 detik

if __name__ == "__main__":
    asyncio.run(monitor_sites())
