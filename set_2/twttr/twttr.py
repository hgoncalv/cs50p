str = input("Input: ")
ret = ""
vowals = {"a","e","i","o","u"}

for c in str:
    if(c.lower() not in vowals):
        ret += c

print(f"Output: {ret}")
