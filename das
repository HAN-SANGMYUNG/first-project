store_name= "Hanstore"
def say_hi(sn):
    print(f"hello wlecome {store_name} good")

Fruits_Menu = {
    "1": ("🍊 Jeju tangerines", 10.99),
    "2": ("🍓 Strawberries", 20.00),
    "3": ("🍎 Apples", 30.00)
}

say_hi(store_name)

for key, (name,fee) in Fruits_Menu.items():
    print(f"{key}. {name} - ${fee} per kg")