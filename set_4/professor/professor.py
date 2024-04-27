import random

def generate_math_problem(level):
    x = generate_integer(level)
    y = generate_integer(level)
    return [x,y,x+y]

def generate_integer(level):
    if not isinstance(level, int) or not (0 < level < 4):
        raise ValueError
    min_value = 0 if level == 1 else 10**(level-1)
    max_value = 10**(level) - 1
    return random.randint(min_value, max_value)

def get_level():
    while True:
        user_input = input("Level: ")
        if user_input.isnumeric():
            num = int(user_input)
            if(not 0<num<4):
                continue
            return num
        else:
            continue

def solve_question(x, y, answer):
    user_input = input(f"{x} + {y} = ")
    if user_input.isnumeric():
        user_answer = int(user_input)
        if answer == user_answer:
            return True
    return False


def play(level, n_problems):
    score = 0
    for _ in range(0, n_problems):
        x,y,answer = generate_math_problem(level)
        for i in range(0,3):
            if not solve_question(x, y, answer):
                print("EEE")
            else:
                score += 1
                break
            if i == 2:
                print(f"{x} + {y} = {answer}")
    return score

def main():

    level = get_level()
    score = play(level, 10)
    print("Score:", score)

if __name__ == "__main__":
    main()
