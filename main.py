# main.py

from menu import tampilkan_menu
from order import tambah_pesanan, tampilkan_keranjang, keranjang_kosong
from payment import proses_pembayaran

def main():
    while True:
        print("\n===== SISTEM PEMESANAN =====")
        print("1. Lihat Menu")
        print("2. Tambah Pesanan")
        print("3. Lihat Keranjang")
        print("4. Bayar")
        print("5. Keluar")
        pilihan = input("Pilih menu [1-5]: ")

        if pilihan == "1":
            tampilkan_menu()
        elif pilihan == "2":
            try:
                menu_id = int(input("Masukkan ID Menu: "))
                jumlah = int(input("Jumlah: "))
                tambah_pesanan(menu_id, jumlah)
            except ValueError:
                print(">> Input tidak valid.")
        elif pilihan == "3":
            tampilkan_keranjang()
        elif pilihan == "4":
            if keranjang_kosong():
                print(">> Keranjang masih kosong.")
            else:
                proses_pembayaran()
        elif pilihan == "5":
            print("Terima kasih. Sampai jumpa!")
            break
        else:
            print(">> Pilihan tidak valid.")

if __name__ == "__main__":
    main()

