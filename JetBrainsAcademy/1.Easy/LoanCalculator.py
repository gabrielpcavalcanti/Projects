import argparse
from math import ceil, pow, log

def isnumber(value):

    try:
         
         float(value)

    except ValueError:
         
         return False
    
    return True

def differentiated_payments(principal, periods, interest):

    i = (float(interest) / 100) / 12
    soma = 0

    for m in range(1,int(periods)+1):

        diff_pay = (float(principal)/float(periods)) + i * ((float(principal)) - ((float(principal) * (m - 1))/ float(periods)))
        print(f"Month {m}: payment is {ceil(diff_pay)}")
        soma += ceil(diff_pay) 

    print()
    print(f"Overpayment = {ceil(soma) - int(principal)}")

def annuity_payment(principal, periods, interest):

    i = (float(interest) / 100) / 12

    A = float(principal) * ((i * pow(1 + i, float(periods))) / (pow(1 + i, float(periods)) - 1))

    print(f"Your annuity payment = {ceil(A)}!")
    print(f"Overpayment = {ceil(A)*int(periods) - int(principal)}")

    return A

def loan_principal(payment, periods, interest):
     
     i = (float(interest) / 100) / 12
     
     P = float(payment) / ((i * pow(1 + i, float(periods))) / (pow(1 + i, float(periods)) - 1))

     print(f"Your loan principal = {ceil(P)}!")
     print(f"Overpayment = {ceil(float(payment) * float(periods) - P)}")

def mouths(payment, principal, interest):
    
    i = (float(interest) / 100) / 12

    n = ceil(log(float(payment) / (float(payment) - i * float(principal)), 1 + i))

    years = n // 12
    months = n % 12

    print(n)

    if years == 1:
        print("It will take 1 year to repay this loan!")
    elif years > 1 and months == 0:
        print(f"It will take {years} year to repay this loan!")
    elif years < 1:
        print(f"It will take {months} months to repay this loan!")
    else:
        print(f"It will take {years} years and {months} months to repay this loan!")

    print(f"Overpayment = {int(n * float(payment) - float(principal))}")

parser = argparse.ArgumentParser()

parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

list_args = [args.type, args.payment, args.principal, args.periods, args.interest]
list_args_not_none = []

for i in list_args:
    if i != None:
        list_args_not_none.append(i)

for n in list_args_not_none:
    number = isnumber(n)
    if number == True:
        if float(n) < 0:
            print("Incorrect parameters")
            break

for k in list_args:
    if args.type not in ["annuity","diff"]:
        print("Incorrect parameters")
        break
    
    elif args.type == None:
        print("Incorrect parameters")
        break

    elif args.type == "diff" and args.payment != None:
        print("Incorrect parameters")
        break

    if args.interest == None:
        print("Incorrect parameters")
        break

    if len(list_args_not_none) != 4:
        print("Incorrect parameters")
        break

if args.type == "diff":
        if list_args[4] == None:
            print()
            print("Incorrect parameters")
        elif list_args[1] == None:
            differentiated_payments(principal=args.principal, periods=args.periods, interest=args.interest)

if args.type == "annuity":
    if list_args[4] == None:
        print()
        print("Incorrect parameters")
    elif list_args[1] == None:
        annuity_payment(principal=args.principal, periods=args.periods, interest=args.interest)
    elif list_args[2] == None:
        loan_principal(payment=args.payment, periods=args.periods, interest=args.interest)
    elif list_args[3] == None:
        mouths(payment=args.payment, principal=args.principal, interest=args.interest)
