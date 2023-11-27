from random import randint


def range_to_generated_nums():
    while True:
        try:
            num_1 = int(input('Enter start of range: '))
            num_2 = int(input('Enter end of range: '))
            return num_1, num_2
        except ValueError:
            print('Expected number, got a string. Try again')


def check_generated_nums():
    while True:
        try:
            min_range, max_range = range_to_generated_nums()
            if max_range - min_range < 5 or max_range - min_range > 30:
                print('The range must include from 5 to 30 numbers. Try again: ')
            else:
                return min_range, max_range
        except ValueError:
            print("Invalid input. Please enter valid integers.")


def generate_three_random_nums():
    num_1, num_2 = check_generated_nums()
    random_nums = [randint(num_1, num_2) for _ in range(3)]
    print(random_nums)
    return set(random_nums)


def user_nums_to_guess():
    user_nums = set()
    for i in range(3):
        num = input('Enter number to guess or \'exit\' to surrender: ')
        if num == 'exit':
            exit()
        num = int(num)
        user_nums.add(num)
    return user_nums


def guessing_generated_nums():
    random_nums = generate_three_random_nums()
    while True:
        user_nums = user_nums_to_guess()
        num_of_matches = len(set(random_nums).intersection(user_nums))
        if num_of_matches == 3:
            print('You win!')
            break
        elif num_of_matches == 2:
            print(f'You guess two of three numbers. Try again!')
        elif num_of_matches == 1:
            print(f'You guess one of three numbers. Try again!')
        else:
            print('No numbers were guessed. Try again!')


guessing_generated_nums()
