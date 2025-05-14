# menu.py

menu_items = [
    {"id": 1, "nama": "Nasi Goreng", "harga": 20000},
    {"id": 2, "nama": "Mie Ayam", "harga": 18000},
    {"id": 3, "nama": "Ayam Bakar", "harga": 25000},
    {"id": 4, "nama": "Es Teh", "harga": 5000}
]

def tampilkan_menu():
    print("\n=== MENU MAKANAN ===")
    for item in menu_items:
        print(f"{item['id']}. {item['nama']} - Rp{item['harga']}")

