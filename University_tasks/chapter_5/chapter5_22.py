from random import randint

number = randint(1, 10)

while True:
    guess = int(input("type your guess 1 -->10 :"))
    if number == guess:
        print("right")
        break
    else:
        print("wrong")