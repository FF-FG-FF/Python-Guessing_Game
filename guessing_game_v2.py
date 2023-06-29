import random

def guessing_game():
    print("1, SINGLEPLAYER")
    print("2, MULTIPLAYER")
    choice = (int(input("Navigate The Menu Using 1-2")))
    
    if choice == 1:
        a = 1
        b = 100
        target_number = random.randint(a,b)
    elif choice == 2:
        a = int(input("Type The Low/Starting Number: "))
        b = int(input("Type The Ending Number: "))
        target_number = random.randint(a,b)
        
    attempts = 0
    
    while True:
        user_guess = int(input(f"Type a guess from {a}-{b}: "))
        attempts += 1 
        
        if user_guess > target_number:
                print("Your Guess Is Too High")
        elif user_guess < target_number:
                print("Your Guess Is Too Low")
        else: 
                print(f"Congrats You Guessed The number '{target_number}' in {attempts} attempts")
                break
            
            
guessing_game()            
        
