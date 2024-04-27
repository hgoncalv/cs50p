def valueReturned(str):
    if(str.startswith("hello")):
        return "$0"
    if(str[0]=="h"):
        return "$20"
    return "$100"

print(valueReturned(input("Greeting: ").strip().lower()))
