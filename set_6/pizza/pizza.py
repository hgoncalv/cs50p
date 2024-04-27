import sys
import csv
from pprint import pprint
from tabulate import tabulate


def get_validated_filename_with_extension(required_extension=None):
    filename = sys.argv[1]
    _, extension = filename.rsplit(".", 1)

    if required_extension is not None and extension != required_extension:
        exit(f"Not a {required_extension.upper()} file")

    return filename


def check_argv_count(expected_arg_count):
    actual_arg_count = len(sys.argv)
    if actual_arg_count > expected_arg_count:
        exit("Too many command-line arguments")
    elif actual_arg_count > expected_arg_count:
        exit("Too few command-line arguments")


def read_non_comment_non_empty_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            stripped_line = line.rstrip()
            if stripped_line and not stripped_line.startswith("#"):
                lines.append(stripped_line)
    return lines


def read_csv_table(filename):
    table = []
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
    return table


def print_table_with_grid(table):
    headers = table[0]
    data = table[1:]
    print(tabulate(data, headers, tablefmt="grid"))


def main():
    check_argv_count(2)
    filename = get_validated_filename_with_extension("csv")
    table = read_csv_table(filename)
    print_table_with_grid(table)


if __name__ == "__main__":
    main()
