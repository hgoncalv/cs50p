import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'
    match = re.search(pattern, s)
    if match:
        video_id = match.group(1)
        youtu_be_url = f"https://youtu.be/{video_id}"
        return youtu_be_url
    else:
        return None


if __name__ == "__main__":
    main()
