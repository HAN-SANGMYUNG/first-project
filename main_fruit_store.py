# 상점 이름
store_name = "Hanstore"

# 상품 목록
Fruits_Menu = {
    "1": ("🍊 Jeju tangerines", 10.99),
    "2": ("🍓 Strawberries", 20.00),
    "3": ("🍎 Apples", 30.00)
}

# 인사 함수
def print_greeting():
    print(f"\n🏪 Welcome to {store_name}!\n")

# 메뉴 출력 함수
def print_menu():
    print("📋 Menu:")
    for key, (product, price) in Fruits_Menu.items():
        print(f"{key}. {product} - ${price:.2f} per kg")
    print("4. 🧺 Empty Basket\n")

# 영수증 출력 함수
def print_receipt(cart):
    if not cart:
        print("🧺 Your basket is empty.\n")
        return
    print("\n🧾 Receipt")
    total = 0
    for product, (quantity, price) in cart.items():
        item_total = quantity * price
        print(f"{product}: {quantity:.2f} kg - ${item_total:.2f}")
        total += item_total
    print(f"\n💰 Total amount due: ${total:.2f}")
    print("🛒 Thank you for visiting!\n")

# 상점 실행 함수
def run_store():
    cart = {}
    print_greeting()

    while True:
        print_menu()
        choice = input("Select item (1-3), 4 to empty basket, or 'QUIT': ").strip().upper()

        if choice == "QUIT":
            print("👋 Goodbye!")
            break
        elif choice == "4":
            cart.clear()
            print("🧺 Basket emptied.\n")
        elif choice in Fruits_Menu:
            product, price = Fruits_Menu[choice]
            qty_input = input(f"How many kg of {product}? (or 'QUIT'): ").strip().upper()
            if qty_input == "QUIT":
                print("👋 Goodbye!")
                break
            try:
                quantity = float(qty_input)
                cart[product] = (cart.get(product, (0, price))[0] + quantity, price)
                print(f"✅ Added {quantity} kg of {product} to your cart.\n")
            except ValueError:
                print("❌ Invalid quantity.\n")
                continue

            next_action = input("Type 'R' for receipt or anything else to continue: ").strip().upper()
            if next_action == "R":
                print_receipt(cart)
        else:
            print("❌ Invalid selection.\n")

# 프로그램 실행
run_store()
