# main.py
from services import authenticate
from roles.customer import customer_menu
from roles.kitchen import kitchen_menu
from roles.admin import admin_menu
from models import UserRole

def main():
    print("🍽️  SELAMAT DATANG DI WAKRUN DIGITAL")
    while True:
        print("\n🔐 Login")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        user = authenticate(username, password)
        if not user:
            print("❌ Login gagal!")
            continue

        print(f"✅ Login berhasil sebagai: {user.role.value.upper()}")
        
        # Routing berdasarkan role
        if user.role == UserRole.CUSTOMER:
            customer_menu(user.user_id)
        elif user.role == UserRole.KITCHEN:
            kitchen_menu()
        elif user.role == UserRole.ADMIN:
            admin_menu()

if __name__ == "__main__":
    main()