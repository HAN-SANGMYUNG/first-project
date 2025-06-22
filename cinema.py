# cinema.py
from store_module import run_store
#수정하는거 알아보기기
product_catalog = {
    "1": ("🎟️ Standard Ticket", 12.00),
    "2": ("🥤 Large Drink", 5.50),
    "3": ("🍿 Popcorn Combo", 8.25),
    "4": ("ddsdsd", 32)
}
store_name = "Grand Cinema"
unit_name = "item(s)"
#안녕하세요요
if __name__ == "__main__":
    run_store(store_name, product_catalog, unit_name)
