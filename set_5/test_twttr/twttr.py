

def main():
    str = input("Input: ")
    print(f"Output: {shorten(str)}")
    print(shorten(123))


def shorten(word):
    ret = ""
    vowals = {"a","e","i","o","u"}
    for c in word:
        if(c.lower() not in vowals):
            ret += c
    return ret



if __name__ == "__main__":
    main()
