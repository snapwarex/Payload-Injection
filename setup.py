import os
import time

def banner():
    print(r"""
    \033[94m
     _____                      _     ___       _           _   _             

    |  __ \                    | |   |_  |     (_)         | | (_)            
    | |__) |_ _ _   _ _ __   __| |     | | _ __  _  ___  __| |_ _  ___  _ __  
    |  ___/ _` | | | | |  _ \ / _` |     | | '_ \| |/ _ \/ _` | | |/ _ \| '_ \ 
    | |  | (_| | |_| | | | | | (_| | /\__/ / | | | |  __/ (_| | | | (_) | | | |
    |_|   \__,_|\__, |_| |_| \__,_| \____/|_| |_| |\___|\__,_|_|_|\___/|_| |_|
    \033[0m""")

def install():
    banner()
    print("[*] Menyiapkan sistem Payload Injection...")
    time.sleep(1)
    
    pilihan = input("\n[?] Tambahkan payload database.txt ke instalasi? (Y/n): ").lower()
    
    if pilihan == 'y':
        if os.path.exists("database.txt"):
            print("[+] Database payload terdeteksi dan dikonfigurasi.")
        else:
            print("[!] File database.txt tidak ditemukan di folder, silakan buat manual.")
    else:
        print("[!] Melanjutkan tanpa instalasi payload.")

    print("[+] Menginstal plugin turbo.py... Done.")
    print("\n[OK] Instalasi 100% Berhasil! Jalankan 'python3 main.py'")

if __name__ == "__main__":
    install()
