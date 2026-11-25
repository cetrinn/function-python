# database.py - Modul 8 Function

def simpan_biodata():
    print("\n--- Menyimpan Biodata ---")
    nama = input("Masukan Nama : ")
    tanggal_lahir = input("Masukan Tanggal Lahir : ")
    asal_daerah = input("Masukan Asal Daerah : ")

    with open("database.txt", "a") as file:
        file.write(f"Nama : {nama}\n")
        file.write(f"Tanggal Lahir : {tanggal_lahir}\n")
        file.write(f"Asal Daerah : {asal_daerah}\n")
        file.write("----------------------------\n")

    print("Biodata berhasil disimpan!")

def tampilkan_biodata():
    print("\n--- Semua Biodata ---")
    try:
        with open("database.txt", "r") as file:
            isi = file.read()
            print(isi)
    except FileNotFoundError:
        print("Belum ada biodata yang tersimpan.")

def main():
    while True:
        print("\n=== MENU ===")
        print("1. Menyimpan biodata")
        print("2. Tampilkan semua biodata")
        print("3. Keluar program")

        pilihan = input("Pilih menu (1/2/3) : ")

        if pilihan == "1":
            simpan_biodata()
        elif pilihan == "2":
            tampilkan_biodata()
        elif pilihan == "3":
            print("Keluar program. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid!")

main()