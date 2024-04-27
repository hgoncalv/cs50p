import random

def get_valid_integer_input(prompt, min_val=None):
    while True:
        user_input = input(prompt).strip()
        if user_input.isnumeric():
            num = int(user_input)
            if min_val is not None and num < min_val:
                continue
            return num

def main():
    while True:
        n = get_valid_integer_input("Level: ", 1)
        if n >= 1:
            break

    game_number = random.randint(1, n)

    while True:
        guess = get_valid_integer_input("Guess: ", 1)
        if guess == game_number:
            print("Just right!")
            break
        elif guess > game_number:
            print("Too large!")
        elif guess < game_number:
            print("Too small!")

if __name__ == "__main__":
    main()
