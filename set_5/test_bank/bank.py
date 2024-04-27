def value(greeting):
    greeting = greeting.strip().lower()
    if(greeting.startswith("hello")):
        return 0
    if(greeting[0]=="h"):
        return 20
    return 100


def main():
    print(f"${value(input("Greeting: "))}")


if __name__ == "__main__":
    main()
