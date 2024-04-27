import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(r'(\d{1,2}):?([0-5][0-9])? (AM|PM) to (\d{1,2}):?([0-5][0-9])? (AM|PM)', s)
    if not match:
        raise ValueError("Invalid input format")

    hour1, minute1, period1, hour2, minute2, period2 = match.groups()

    def adjust_hour(hour, period):
        hour = int(hour)
        if period == "PM" and hour != 12:
            hour += 12
        elif period == "AM" and hour == 12:
            hour = 0
        return f"{hour:02d}"

    return f"{adjust_hour(hour1, period1)}:{minute1 or '00'} to {adjust_hour(hour2, period2)}:{minute2 or '00'}"

if __name__ == "__main__":
    main()
