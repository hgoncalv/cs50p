import sys
import csv
from pprint import pprint
from tabulate import tabulate

def file_to_list(filename):
    list = []
    with open(filename) as file:
        for line in file:
            tmp = line.rstrip()
            if line.strip() and not line.startswith("#"): #strip returns True if the line only has spaces or \n
                list.append(tmp)
    return(list)

def csv_to_table(filename):
    table = []
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            table.append(row)
    return table

def print_table_with_grid(table):
    headers = table[0]
    table = table[1:]
    print(tabulate(table, headers, tablefmt="grid"))



def main():
    if(len(sys.argv) !=2):
        exit("please insert filename")
    filename = sys.argv[1]
    extension = filename[filename.index("."):]

    if(extension != ".csv"):
        exit("not a Python file")

    table = csv_to_table(filename)
    print_table_with_grid(table)


if __name__ == "__main__":
    main()
