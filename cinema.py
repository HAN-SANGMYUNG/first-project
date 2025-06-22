# cinema.py
from store_module import run_store

product_catalog = {
    "1": ("🎟️ Standard Ticket", 12.00),
    "2": ("🥤 Large Drink", 5.50),
    "3": ("🍿 Popcorn Combo", 8.25)
}
store_name = "Grand Cinema"
unit_name = "item(s)"

if __name__ == "__main__":
    run_store(store_name, product_catalog, unit_name)
