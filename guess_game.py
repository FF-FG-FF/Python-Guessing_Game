import random #imports the random module from the python library so we can use the random.randint(a,b) function

def random_number():
    target_num = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Guess a Number Between 1 and 100:"))
        attempts += 1
        
        if guess < target_num:
            print("Number is too low")
        elif guess > target_num:
             print("Number is too high")
        else:
            print(f"congrats you won in {attempts} attempts")
            break

    
random_number() #required to start the function(or any) , without it the game woudlnt start