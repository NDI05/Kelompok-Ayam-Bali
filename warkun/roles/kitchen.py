# roles/kitchen.py
from models import OrderStatus
from services import get_orders_by_status, ORDERS

def kitchen_menu():
    while True:
        print("\n👨‍🍳 [DAPUR] Menu:")
        print("1. Lihat Pesanan Baru (PAID)")
        print("2. Tandai Pesanan Selesai")
        print("3. Lihat Semua Pesanan")
        print("4. Logout")
        choice = input("Pilih: ").strip()

        if choice == "1":
            new_orders = get_orders_by_status(OrderStatus.PAID)
            if new_orders:
                print("\n🔔 Pesanan Baru:")
                for o in new_orders:
                    print(f"- {o}")
            else:
                print("Tidak ada pesanan baru.")

        elif choice == "2":
            order_id = input("Masukkan ID Pesanan (misal: ORD001): ").strip()
            for order in ORDERS:
                if order.order_id == order_id and order.status == OrderStatus.IN_KITCHEN:
                    order.status = OrderStatus.READY
                    print(f"✅ Pesanan {order_id} ditandai SELESAI.")
                    break
            else:
                print("❌ Pesanan tidak ditemukan atau belum diproses.")

        elif choice == "3":
            for o in ORDERS:
                print(f"- {o}")

        elif choice == "4":
            break