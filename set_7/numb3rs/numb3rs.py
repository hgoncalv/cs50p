import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    valid = False
    octet_pattern = r"(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    pattern = r"^(?:%s\.){3}(?:%s)$" % (octet_pattern, octet_pattern)
    if matches := re.search(pattern, ip):
        valid = True
    return valid


if __name__ == "__main__":
    main()
