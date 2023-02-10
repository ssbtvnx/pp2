import random
s=input("Hello! What is your name? \n")
print(f'Well,{s}, I am thinking of a number between 1 and 20.')

x=random.randint(1,21) # 2
guesses=0
while True:
    number=int(input())
    guesses+=1
    if number==x:
        print("Good job,",  s, "You guessed my number in", guesses, "guesses!")
        break
    elif number<x:
        print("Your guess is too low.")
    else:  
        print("Your guess is too high.")