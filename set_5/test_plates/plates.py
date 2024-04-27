def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 2 <=len(s) <= 6 :
        return False
    if not s.isalnum():
        return False
    if any(c.isnumeric() for c in s[:2]):
        return False

    found_numeric = False
    for i, char in enumerate(s):
        if char.isnumeric():
            if not found_numeric and char == "0":
                return False
            found_numeric = True
        elif found_numeric:
            return False
    return True

if __name__ == "__main__":
    main()
