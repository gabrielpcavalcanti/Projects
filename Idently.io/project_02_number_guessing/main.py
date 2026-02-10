from random import randint

LOWER_NUMBER:int = 1
HIGHEST_NUMBER:int = 10

price:int = randint(LOWER_NUMBER, HIGHEST_NUMBER)

def guessing_game() -> None:
    
    while True:
        
        try:
            guess_number: int = int(input("Type a number: "))
            
        except ValueError as e:
            print("Please, enter a valid number.")
            continue
        
        if guess_number == price:
            print("You won!")
            break
        
        elif guess_number < price:
            print("it is higher number")
            
        elif guess_number > price:
            print("It is a lower number")

def main() -> None: 
    
    print(f'Try to guess a number between {LOWER_NUMBER} and {HIGHEST_NUMBER}')
    
    guessing_game()
        
        
if __name__ == "__main__":
    main()