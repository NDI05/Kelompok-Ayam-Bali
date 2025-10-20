# roles/customer.py
from models import Order, OrderItem, OrderStatus
from services import MENU_ITEMS, ORDERS

def customer_menu(user_id: str):
    while True:
        print("\n👤 [PELANGGAN] Menu:")
        print("1. Lihat Menu")
        print("2. Pesan Makanan")
        print("3. Lihat Riwayat Pesanan")
        print("4. Logout")
        choice = input("Pilih: ").strip()

        if choice == "1":
            print("\n📋 Menu:")
            for i, item in enumerate(MENU_ITEMS, 1):
                print(f"{i}. {item}")

        elif choice == "2":
            table = input("🪑 Nomor meja: ").strip()
            order = Order(f"ORD{len(ORDERS)+1:03d}", table, user_id)
            while True:
                print("\nPilih menu (ketik 'selesai' untuk bayar):")
                item_choice = input("Nomor: ").strip()
                if item_choice.lower() == "selesai":
                    break
                try:
                    idx = int(item_choice) - 1
                    if 0 <= idx < len(MENU_ITEMS):
                        item = MENU_ITEMS[idx]
                        qty = int(input(f"Jumlah {item.name}: "))
                        notes = input("Catatan (opsional): ").strip()
                        order.add_item(OrderItem(item, qty, notes))
                    else:
                        print("❌ Menu tidak valid")
                except ValueError:
                    print("❌ Input tidak valid")
            
            if order.items:
                total = order.calculate_total()
                print(f"\n💰 Total: Rp{total:.0f}")
                if input("Bayar? (y/n): ").lower() == "y":
                    if order.pay():
                        ORDERS.append(order)
                        print("✅ Pembayaran berhasil! Notifikasi dikirim ke dapur.")
                    else:
                        print("❌ Gagal bayar.")
            else:
                print("Tidak ada pesanan.")

        elif choice == "3":
            my_orders = [o for o in ORDERS if o.customer_id == user_id]
            if my_orders:
                for o in my_orders:
                    print(f"- {o}")
            else:
                print("Belum ada pesanan.")

        elif choice == "4":
            break