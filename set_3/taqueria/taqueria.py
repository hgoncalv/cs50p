MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def run():
    total=0
    while True:
        try:
            user_input = input("Item: ").lower().title()
            if(user_input in MENU):
                total += MENU[user_input]
                print(f"Total: ${total:.2f}")
        except EOFError:
            break

def main():
    run()


if __name__ == "__main__":
    main()
