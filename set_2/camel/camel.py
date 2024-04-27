str = input("camelCase:")
ret = ""

for i, c in enumerate(str):
    if(c.isupper() and i > 0):
        ret+="_"
    ret += c.lower()

print(f"snake_case: {ret}")
