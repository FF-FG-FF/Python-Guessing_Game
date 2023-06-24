import random

def guessing_game():
    a = int(input("Enter the low/Initial number: "))
    b = int(input("Enter the High/Ending number: "))
    target_number = random.randint(a,b)
    attempts = 0
    
    while True:
        user_guess = int(input(f"Guess a number Between {a} and {b}: "))
        attempts += 1
        
        if user_guess < target_number:
            print("The Guess is too low")
        elif user_guess > target_number:
            print("The Guess Is too high")
        else: 
            print(f"Congrats you guessed the number in {attempts} attempts")
            
guessing_game()            