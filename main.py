import turbo
import os

def main():
    os.system('clear')
    print("\033[91m")
    print("="*50)
    print("      PAYLOAD INJECTION TOOLS BY SNAPWAREX")
    print("="*50)
    print("\033[0m")
    
    target = input("[?] Target URL (contoh: http://test.com): ")
    
    if not os.path.exists("database.txt"):
        print("[!] Error: database.txt hilang!")
        return

    with open("database.txt", "r") as f:
        payloads = [line.strip() for line in f.readlines() if line.strip()]

    print(f"\n[+] {len(payloads)} Payload siap digunakan.")
    print("\nMenu:")
    print("1. Manual Mode (Satu per satu)")
    print("2. Turbo Mode (Otomatis & Cepat)")
    
    pilih = input("\nPilih opsi: ")

    if pilih == "2":
        turbo.run_turbo(target, payloads)
    else:
        for p in payloads:
            print(f"\n[*] Menguji: {p}")
            turbo.request_worker(target, p)
            input("Tekan Enter untuk lanjut...")

if __name__ == "__main__":
    main()
