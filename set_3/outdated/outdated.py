import datetime

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def convert_date(month, day, year):
    try:
        datetime_obj = datetime.datetime(year, month, day)
        return datetime_obj.strftime("%Y-%m-%d")
    except ValueError:
        return None

def parse_date(date_str):
    try:
        date_arr = date_str.split("/")
        if len(date_arr) != 3:
            date_arr = date_str.split(" ")
            if len(date_arr) == 3:
                day = int(date_arr[1][:-1])
                month = MONTHS.index(date_arr[0]) + 1
                year = int(date_arr[2])
            else:
                return None
        else:
            month, day, year = map(int, date_arr)
        return convert_date(month, day, year)
    except (ValueError, IndexError):
        return None

def get_user_input(prompt):
    try:
        yield input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        pass

def main():
    while True:
        date_str = next(get_user_input("date: "))
        date_arr = parse_date(date_str)
        if date_arr is None:
            continue
        else:
            print(date_arr)
            break

if __name__ == "__main__":
    main()
