from datetime import date
import datetime
import inflect
import sys

p = inflect.engine()


def get_date_delta(date_str):

    try:
        # Split the user input by "-" and parse each substring into an integer
        year, month, day = map(int, date_str.split("-"))

        # Create a date object from the parsed integers
        date_from_user = date(year, month, day)


        # Calculate the difference between the user's date of birth and today's date
        delta = datetime.date.today() - date_from_user

        return p.number_to_words(delta.days* 24 * 60, andword="").capitalize() + " minutes"
    except ValueError:
        return None



def main():
    user_input = input("Date of Birth (YYYY-MM-DD): ")
    min_interval = get_date_delta(user_input)
    if min_interval is not None:
        print(min_interval)
    else:
        sys.exit("Invalid date format.")



if __name__ == "__main__":
    main()
