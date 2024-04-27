import inflect

p = inflect.engine()

def get_user_input(prompt):
    try:
        while True:
            yield input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        pass

def main():
    names = []
    for name in get_user_input("Names: "):
        names.append(name)
    print("Adieu, adieu, to",p.join(names))

if __name__ == "__main__":
    main()
