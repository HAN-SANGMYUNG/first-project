# store_module.py

def print_greeting(store_name):
    print(f"\n🏪 Welcome to {store_name}!\n")

def print_menu(product_catalog, unit_name):
    print("📋 Menu:")
    for key, (product, price) in product_catalog.items():
        print(f"{key}. {product} - ${price:.2f} per {unit_name}")
    print("4. 🧺 Empty Basket\n")

def print_receipt(cart, product_catalog, unit_name):
    print("\n🧾 Receipt")
    total = 0
    for key, (product, price) in product_catalog.items():
        quantity = cart.get(product, (0, price))[0]
        item_total = quantity * price
        print(f"{product}: {quantity:.2f} {unit_name} - ${item_total:.2f}")
        total += item_total
    print(f"\n💰 Total amount due: ${total:.2f}")
    print("🛒 Thank you for visiting!\n")


def run_store(store_name, product_catalog, unit_name):
    while True:
        cart = {}
        print_greeting(store_name)
        
        while True:
            print_menu(product_catalog, unit_name)
            print("Please select a menu number (1-3).")
            print("To empty your basket, enter 4.")
            print("To quit, type 'QUIT'.\n")

            choice = input("Your choice: ").strip().upper()

            if choice == "QUIT":
                print("👋 Goodbye!")
                return
            elif choice == "4":
                cart.clear()
                print("🧺 Basket emptied.\n")
                continue
            elif choice in product_catalog:
                product_name, price = product_catalog[choice]
                try:
                    quantity_input = input(f"How many {unit_name} of {product_name}? (Type 'QUIT' to exit): ").strip().upper()
                    if quantity_input == "QUIT":
                        print("👋 Goodbye!")
                        return
                    quantity = float(quantity_input)
                    if quantity < 0:
                        print("⚠️ Please enter a non-negative number.\n")
                        continue
                    if product_name in cart:
                        cart[product_name] = (cart[product_name][0] + quantity, price)
                    else:
                        cart[product_name] = (quantity, price)
                    print(f"✅ Added {quantity} {unit_name} of {product_name} to your cart.\n")
                except ValueError:
                    print("❌ Invalid input. Please enter a valid number.\n")
            else:
                print("❌ Invalid menu selection. Try again.\n")
                continue

            next_action = input("Type 'R' to view receipt or 'M' to return to the menu: ").strip().upper()
            if next_action == "QUIT":
                print("👋 Goodbye!")
                return
            elif next_action == "R":
                if cart:
                    print_receipt(cart, product_catalog, unit_name)
                else:
                    print("🧺 Your basket is empty.\n")
                break
            elif next_action == "M":
                continue
            else:
                print("Invalid input, returning to menu...\n")
