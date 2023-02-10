import random
guess = random.randint(0, 20)

cnt = 0 

print("Hello! What is your name?")
name = input()

print("Well, KBTU, I am thinking of a number between 1 and 20.\n" "Take a guess")
user = int(input())

while user != guess:
    cnt += 1
    if user < guess :
        print("Your guess is too low")
        user = int(input())
    else:
        print("Your guess is too high")
        user = int(input())

print("Good job, KBTU! You guessed my number in {} guesses!".format(cnt + 1))