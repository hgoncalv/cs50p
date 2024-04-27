def get_percent():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = map(int, fraction.split('/'))

            if x > y or y == 0:
                raise ValueError

            percentage = x / y * 100

            if percentage <= 1:
                return 'E'
            elif percentage >= 99:
                return 'F'
            else:
                return round(percentage)
        except (ValueError, ZeroDivisionError):
            continue

def main():
    fuel_percentage = get_percent()
    print(f"{fuel_percentage}%" if type(fuel_percentage) == int else fuel_percentage)

if __name__ == "__main__":
    main()
