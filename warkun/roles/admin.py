# roles/admin.py
from datetime import datetime
from services import ORDERS

def admin_menu():
    while True:
        print("\n🛡️ [ADMIN] Menu:")
        print("1. Lihat Semua Pesanan")
        print("2. Generate Laporan Bulanan")
        print("3. Logout")
        choice = input("Pilih: ").strip()

        if choice == "1":
            for o in ORDERS:
                print(f"- {o}")

        elif choice == "2":
            completed = [o for o in ORDERS if o.status.name in ["READY", "COMPLETED"]]
            revenue = sum(o.total_amount for o in completed)
            print(f"\n📈 LAPORAN BULANAN ({datetime.now().strftime('%B %Y')}):")
            print(f"Total Pesanan Selesai: {len(completed)}")
            print(f"Total Pendapatan: Rp{revenue:.0f}")
            for o in completed:
                print(f"  - {o}")

        elif choice == "3":
            break