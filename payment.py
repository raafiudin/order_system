# payment.py

from order import hitung_total

def proses_pembayaran():
    total = hitung_total()
    print(f"\nTotal yang harus dibayar: Rp{total}")
    try:
        uang = int(input("Masukkan jumlah uang: Rp"))
        if uang >= total:
            kembalian = uang - total
            print(f"Pembayaran berhasil. Kembalian: Rp{kembalian}")
        else:
            print(">> Uang tidak cukup. Transaksi dibatalkan.")
    except ValueError:
        print(">> Input tidak valid.")

