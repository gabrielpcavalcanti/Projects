import random

def possible_numbers(x, p):
    lista_0 = [num for num in range(x)]
    lista_1 = [num for num in range(1, x)]
    lista_final = []

    if p == 3:

        for i, j in zip(lista_1, lista_0):
            n = 3 * i + j
            lista_final.append(n)
        return lista_final
    
    if p == 5:

        for i, j in zip(lista_1, lista_0):
            n = 5 * i - j
            lista_final.append(n)
        return lista_final


while True:

    try:
        x = int(input("How many pencils would you like to use:"))

        if x < 0:
            print("The number of pencils should be numeric")
            continue
        
        if x == 0:
            print("The number of pencils should be positive")
            continue

        if x and x > 0:
            break

    except ValueError:
        print("The number of pencils should be numeric")
        continue


name_1 = "John"
name_2 = "Jack"

names = [name_1, name_2]

while True:

    name = input(f"Who will be the first ({name_1}, {name_2}):")

    if name in names:
        break

    if name not in names:
        print(f"Choose between {name_1} and {name_2}")
        continue


if name == name_1:
    print("|" * x)
    print(f"{name} turn! ")
    
if name == name_2:
    print("|" * x)
    print(f"{name} turn: ")

while x > 0:

    values = [1,2,3]


    if name == name_2:

        list_3 = possible_numbers(x=x, p=3)
        list_5 = possible_numbers(x=x, p=5)

        if x == 1:
            print("1")
            name = name_1
            print(f"{name} won!")
            break

        if x in list_5:
            m = random.choice([1,2,3])
            x -= m
            print(m)
            print("|" * x)
            name = name_1

            if x == 1:
                print(f"{name} turn! ")
                
                continue
                
            print(f"{name} turn! ")
            continue

        if x % 4 == 0:
            x -= 3
            print("3")
            print("|" * x)
            name = name_1

            if x == 1:
                print(f"{name} turn! ")
                
                continue
                
            print(f"{name} turn! ")
            continue
        
        if x in list_3:
            x -= 2
            print("2")
            print("|" * x)

            name = name_1
            if x == 1:
                print(f"{name} turn! ")
                continue
                
            print(f"{name} turn! ")
            continue

        if x % 2 == 0 and x // 2 in [num for num in range(x) if num % 2 != 0]:
            x -= 1
            print("1")
            print("|" * x)

            name = name_1
            if x == 1:
                print(f"{name} turn! ")
                continue
                
            print(f"{name} turn! ")
            continue


    try:

        drop = int(input())

    except ValueError:
        print("The number of pencils should be numeric")
    
    if drop not in values:
        print("Possible values: '1', '2' or '3'")
        continue
    
    if drop > x:
        print("Too many pencils were taken")
        continue

    x -= drop

    print("|" * x)

    if x <= 0:
        if name == name_1:
            name = name_2
            print(f"{name} won!")
            break
        if name == name_2:
            name = name_1
            print(f"{name} won!")
            break

    if name == name_1:
        name = name_2
        print(f"{name} turn: ")
        continue
    