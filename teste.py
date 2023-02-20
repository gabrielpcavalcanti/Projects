import random

class Bank:

    def __init__(self):

        self.firsts_digits = 400_000
        self.cards_pin = {}
        self.exit_option = True
        self.option = 0


    def generate_number_card(self):

        self.sec_part_digits = ''.join([str(random.randint(0, 9)) for x in range(9)])

        self.last_digit = str(random.randint(0,9))

        self.number_card = int(str(self.firsts_digits) + self.sec_part_digits + self.last_digit)

        return self.number_card
        

    def generate_pin(self):

        self.pin = int(''.join([str(random.randint(0, 9)) for p in range(4)]))

        return self.pin
    
    
    def balance(self):
        
        self.balance_value = 0

        return f"Balance: {self.balance_value}"


    def log_out(self):

        print("You have successfully logged out!")
    
    
    def exit(self):

        print("Bye")
    

    def create_account(self):

        print("Your card has been created")
        print("Your card number:")
        print(self.generate_number_card())

        print("Your card PIN:")
        print(self.generate_pin())

        self.cards_pin[self.number_card] = self.pin


    def log_in(self):

        print("Enter your card number:")

        self.card_number = int(input())

        print("Enter your PIN:")

        self.card_pin = int(input())

        self.trupe_card_number_pin = (self.card_number, self.card_pin)

        self.c = 0

        if self.card_number not in self.cards_pin.keys() or self.pin not in self.cards_pin.values():

            print("Wrong card number or PIN!")
        
        if self.card_number in self.cards_pin.keys() and self.pin in self.cards_pin.values():

            while True:

                if self.c >= len(list(self.cards_pin.items())):

                    print("Wrong card number or PIN!")
                    break

                if self.trupe_card_number_pin == list(self.cards_pin.items())[self.c]:

                    print("You have successfully logged in!")

                    print("1. Balance")
                    print("2. Log out")
                    print("0. Exit")
                    
                    self.option = int(input())

                    if self.option == 1:

                        print(self.balance())
                    
                    elif self.option == 2:
                        
                        self.log_out()
                        break
                    
                    elif self.option == 0:

                        self.exit_option =  False

                        self.exit()
                        break

                else:
                    self.c += 1
                    continue
        
    def open_account(self):

        while True:

            print("1. Create an account")             
            print("2. Log into account")  
            print("0. Exit")

            self.option = int(input())

            if self.option == 1:

                self.create_account()
                continue

            if self.option == 2:

                self.log_in()

                if self.exit_option == False:
                    break

                continue

            if self.option == 0:

                self.exit()
                break

            break


new = Bank()

new.open_account()