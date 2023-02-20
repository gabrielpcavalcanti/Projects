import random


class Bank:

    def __init__(self):

        self.firsts_digits = 400_000
        self.cards_pin = {}
        self.exit_option = True
        self.option = 0
        self.l_num_card = []
        self.l_num2_card = []
        self.l_num3_card = []
        self.l_num_card_luhn = []
        self.sec_part_digits = 0
        self.last_digit = 0
        self.number_card = 0
        self.num_card = 0
        self.card_number = 0
        self.pin = 0
        self.balance_value = 0
        self.card_pin = 0
        self.tuple_card_number_pin = ()
        self.c = 0

    def generate_number_card(self):

        while True:

            self.sec_part_digits = ''.join([str(random.randint(0, 9)) for _ in range(9)])

            self.last_digit = str(random.randint(0, 9))

            self.number_card = int(str(self.firsts_digits) + self.sec_part_digits + self.last_digit)

            self.l_num_card = [int(x) for x in str(self.number_card)]

            self.num_card = self.luhn_algorithm()

            if self.num_card:
                return self.num_card
                
            else:
                self.l_num_card = []
                self.l_num2_card = []
                self.l_num3_card = []
                continue

    def generate_pin(self):

        self.pin = int(''.join([str(random.randint(0, 9)) for _ in range(4)]))

        return self.pin

    def luhn_algorithm(self):

        while True:

            self.l_num_card.pop()
        
            for i in range(0, len(self.l_num_card)):

                if i % 2 == 0:
                    self.l_num2_card.append(self.l_num_card[i]*2)
                else:
                    self.l_num2_card.append(self.l_num_card[i])
        
            for p in self.l_num2_card:

                if p > 9:
                    self.l_num3_card.append(p-9)
                else:
                    self.l_num3_card.append(p)
        
            self.l_num3_card.append(int(self.last_digit))
       
            if list(divmod(sum(self.l_num3_card), 10))[1] == 0:

                return self.number_card
        
            else:
                break

    def balance(self):
        
        self.balance_value = 0

        return f"Balance: {self.balance_value}"

    def create_account(self):

        print("Your card has been created")
        print("Your card number:")
        print((self.generate_number_card()))

        print("Your card PIN:")
        print(self.generate_pin())

        self.cards_pin[self.number_card] = self.pin

    def log_in(self):

        print("Enter your card number:")

        self.card_number = int(input())

        print("Enter your PIN:")

        self.card_pin = int(input())

        self.tuple_card_number_pin = (self.card_number, self.card_pin)

        self.c = 0

        if self.card_number not in self.cards_pin.keys() or self.pin not in self.cards_pin.values():

            print("Wrong card number or PIN!")
        
        if self.card_number in self.cards_pin.keys() and self.pin in self.cards_pin.values():

            while True:

                if self.c >= len(list(self.cards_pin.items())):

                    print("Wrong card number or PIN!")
                    break

                if self.tuple_card_number_pin == list(self.cards_pin.items())[self.c]:

                    print("You have successfully logged in!")

                    print("1. Balance")
                    print("2. Log out")
                    print("0. Exit")
                    
                    self.option = int(input())

                    if self.option == 1:

                        print(self.balance())
                    
                    elif self.option == 2:
                        
                        print("You have successfully logged out!")
                        break
                    
                    elif self.option == 0:

                        self.exit_option = False

                        print("Bye")
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

                if self.exit_option is False:
                    break

                continue

            if self.option == 0:

                print("Bye")
                break

            break


new = Bank()

new.open_account()
