import sys
import csv
from pprint import pprint
from tabulate import tabulate
import PIL
from PIL import Image, ImageOps


def get_file_extension(filename: str) -> str:
    _, extension = filename.rsplit(".", 1)
    return extension.lower()


def get_validated_filename_with_extension(filename, required_extension=None):
    extension = get_file_extension(filename)

    if required_extension is not None and extension not in required_extension:
        exit(f"Not a {required_extension.upper()} file")

    return filename


def check_argv_count(expected_arg_count):
    actual_arg_count = len(sys.argv)
    if actual_arg_count > expected_arg_count:
        exit("Too many command-line arguments")
    elif actual_arg_count < expected_arg_count:
        exit("Too few command-line arguments")


def read_non_comment_non_empty_lines(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            stripped_line = line.rstrip()
            if stripped_line and not stripped_line.startswith("#"):
                lines.append(stripped_line)
    return lines


def read_csv_table_2_list(filename):
    table = []
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
    return table


def split_1col(original_dict: dict, fields: list) -> dict:
    ret = {}
    original, first, last = fields
    for key, value in original_dict.items():
        if key != original:
            ret[key] = value
        else:
            # strip after spliting
            ret[last], ret[first] = (
                component.strip() for component in value.split(",")
            )
    ret = sort_dict_by_keys_by_loop(ret, ["first", "last", "house"])
    return ret


def sort_dict_by_keys_by_sorted(original_dict: dict, key_order: list) -> dict:
    # turn dict to array of duplets. then for each duplet see in key_order what index it should have (index of x[0])
    sorted_items = sorted(original_dict.items(), key=lambda x: key_order.index(x[0]))
    return dict(sorted_items)


def sort_dict_by_keys_by_loop(original_dict: dict, key_order: list) -> dict:
    ret = {}
    for key in key_order:
        if key in original_dict:
            ret[key] = original_dict[key]
    return ret


def read_csv_table_2_dict(filename):
    table = []
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row = split_1col(row, ["name", "first", "last"])
            table.append(row)
    return table


def print_table_with_grid(table):
    headers = table[0]
    data = table[1:]
    print(tabulate(data, headers, tablefmt="grid"))


def write_to_csv_by_order(
    filename: str, table: list[dict[str, str]], order: list
) -> None:
    with open(filename, "w", newline="") as file:
        fieldnames = order
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write the header row with field names
        for row in table:
            writer.writerow(row)


def write_to_csv(filename: str, table: list[dict[str, str]]) -> None:
    with open(filename, "w", newline="") as file:
        fieldnames = table[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write the header row with field names
        for row in table:
            writer.writerow(row)


def main():
    check_argv_count(3)
    allowed_extensions = ["jpg", "jpeg", "png"]
    for file in sys.argv[1:]:
        get_validated_filename_with_extension(file, allowed_extensions)
    if get_file_extension(sys.argv[1]) != get_file_extension(sys.argv[2]):
        exit("Input and output have different extensions")

    shirt_image = Image.open("shirt.png")
    bk_image = Image.open(sys.argv[1])

    bk_image = ImageOps.fit(bk_image, shirt_image.size)
    bk_image.paste(shirt_image, shirt_image)

    bk_image.show()
    bk_image.save(sys.argv[2])


if __name__ == "__main__":
    main()
