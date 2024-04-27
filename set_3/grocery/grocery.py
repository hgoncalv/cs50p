def get_input():
    items ={}
    while True:
        try:
            user_input = input("").upper()
            items[user_input] = items.get(user_input, 0) + 1
        except EOFError:
            break
    return items

def main():
    items_dict = get_input()
    for key in sorted(items_dict):
        print(f"{items_dict[key]} {key}")

if __name__ == "__main__":
    main()
