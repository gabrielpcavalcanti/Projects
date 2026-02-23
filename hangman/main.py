from random import choice

SECRET_WORD = choice(["secret", "apple", "banana"])
chances = 3
blanks: int = 0

def hangman() -> None:
    
    while chances > 0:
        
        print("Word: ", end='')
        
        for char in SECRET_WORD:
            if char in guessed:
                
            
        
def main() -> None:
    
    name: str = input("What is your name? >> ")
    
    print(f'Welcome to hangman, {name}!')

if __name__ == "__main__":
    main()