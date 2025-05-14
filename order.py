# order.py

from menu import menu_items

keranjang = []

def cari_menu_by_id(menu_id):
    for item in menu_items:
        if item["id"] == menu_id:
            return item
    return None

def tambah_pesanan(menu_id, jumlah):
    item = cari_menu_by_id(menu_id)
    if item:
        keranjang.append({
            "item": item,
            "jumlah": jumlah
        })
        print(f">> {item['nama']} x{jumlah} ditambahkan ke keranjang.")
    else:
        print(">> Menu tidak ditemukan.")

def tampilkan_keranjang():
    if not keranjang:
        print(">> Keranjang kosong.")
        return

    print("\n=== KERANJANG PESANAN ===")
    total = 0
    for item in keranjang:
        nama = item["item"]["nama"]
        harga = item["item"]["harga"]
        jumlah = item["jumlah"]
        subtotal = harga * jumlah
        print(f"{nama} x{jumlah} = Rp{subtotal}")
        total += subtotal
    print(f"Total Sementara: Rp{total}")

def hitung_total():
    return sum(item["item"]["harga"] * item["jumlah"] for item in keranjang)

def keranjang_kosong():
    return len(keranjang) == 0

