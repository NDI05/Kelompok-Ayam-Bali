# services.py
from typing import List, Optional
from models import User, Order, MenuItem, UserRole, OrderStatus


# 🔗 Data bersama (shared state) — semua role akses data yang sama
USERS: List[User] = [
    User("C001", "pelanggan", "123", UserRole.CUSTOMER),
    User("K001", "dapur", "123", UserRole.KITCHEN),
    User("A001", "admin", "123", UserRole.ADMIN),
]

MENU_ITEMS: List[MenuItem] = [
    MenuItem("M01", "Nasi Goreng", 18000, "Utama"),
    MenuItem("M02", "Mie Goreng", 16000, "Utama"),
    MenuItem("M03", "Es Teh", 5000, "Minuman"),
    MenuItem("M04", "Ayam Goreng", 20000, "Utama"),
]

ORDERS: List[Order] = []

def authenticate(username: str, password: str) -> Optional[User]:
    for user in USERS:
        if user.username == username and user.password == password:
            return user
    return None

def get_orders_by_status(status: OrderStatus) -> List[Order]:
    return [o for o in ORDERS if o.status == status]

def get_all_orders() -> List[Order]:
    return ORDERS