import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    tuples_list = re.findall(r'(\W|^)um(\W|$)', s, re.IGNORECASE)

    return(len(tuples_list))



if __name__ == "__main__":
    main()
