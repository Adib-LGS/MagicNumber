import random


def ask_number(min_num, max_num):
    number_int = 0
    while number_int == 0:
        number_str = input(f"Eter the magic number between {min_num} and {max_num} ? ")
        try:
            number_int = int(number_str)
        except:
            print("You must enter a Digit")
        else:
            if number_int < min_num or number_int > max_num:
                print(f"Numbers must be between {min_num} and {max_num}")
                number_int = 0
    return number_int


MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)
PLAYERSLIFE = 3

number = 0
win = False
for i in range(0, PLAYERSLIFE):
    life = PLAYERSLIFE - i
    number = ask_number(MIN_NUMBER, MAX_NUMBER)
    if number == MAGIC_NUMBER:
        print("Well Done !")
        win = True
        break
    elif number > MAGIC_NUMBER:
        print("To high")
        print(f"Only {life} before die")
    else:
        print("To Low")
        print(f"Only {life} before die")
if not win:
    print("You Loose !")
"""number = 0
life = PLAYERSLIFE

while number != MAGIC_NUMBER and life > 0:
    number = ask_number(MIN_NUMBER, MAX_NUMBER)
    if number == MAGIC_NUMBER:
        print("Well Done !")
    elif number > MAGIC_NUMBER:
        print("To high")
        life -= 1
        print(f"Only {life} before die")
    else:
        print("To Low")
        life -= 1
        print(f"Only {life} before die")
if life == 0:
    print("You loose")"""