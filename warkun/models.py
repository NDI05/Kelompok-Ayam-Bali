# models.py
from datetime import datetime
from enum import Enum
from typing import List, Optional

class UserRole(Enum):
    CUSTOMER = "customer"
    KITCHEN = "kitchen"
    ADMIN = "admin"

class User:
    def __init__(self, user_id: str, username: str, password: str, role: UserRole):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

class OrderStatus(Enum):
    PENDING = "PENDING"
    PAID = "PAID"
    IN_KITCHEN = "IN_KITCHEN"
    READY = "READY"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class MenuItem:
    def __init__(self, menu_id: str, name: str, price: float, category: str, is_available: bool = True):
        self.menu_id = menu_id
        self.name = name
        self.price = price
        self.category = category
        self.is_available = is_available

    def __repr__(self):
        return f"{self.name} (Rp{self.price})"

class OrderItem:
    def __init__(self, menu_item: MenuItem, quantity: int, special_notes: str = ""):
        self.menu_item = menu_item
        self.quantity = quantity
        self.special_notes = special_notes

    def subtotal(self) -> float:
        return self.menu_item.price * self.quantity

class Order:
    def __init__(self, order_id: str, table_number: str, customer_id: str):
        self.order_id = order_id
        self.table_number = table_number
        self.customer_id = customer_id
        self.order_time = datetime.now()
        self.status = OrderStatus.PENDING
        self.items: List[OrderItem] = []
        self.total_amount = 0.0

    def add_item(self, item: OrderItem):
        self.items.append(item)

    def calculate_total(self) -> float:
        self.total_amount = sum(item.subtotal() for item in self.items)
        return self.total_amount

    def pay(self) -> bool:
        if self.total_amount > 0:
            self.status = OrderStatus.PAID
            return True
        return False

    def __repr__(self):
        items_str = ", ".join([f"{i.quantity}x {i.menu_item.name}" for i in self.items])
        return f"[{self.order_id}] Meja {self.table_number} | {items_str} | Total: Rp{self.total_amount:.0f} | Status: {self.status.value}"