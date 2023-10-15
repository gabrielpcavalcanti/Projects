import random

vic = []

def number_generate(start, finsh, step=1):

    list_num = []

    for i in range(start, finsh, step):
        list_num.append(i)
    
    return list_num


def multiply_by_11(range_num):

    num = random.choice(range_num)

    res_res = int(num) * 11 

    print(f"Calcule o valor de: {num} x 11")
    res = int(input("Digite a resposta: "))

    if res == res_res:
        vic.append(1)
        
    return vic

def square_end_5(range_num):

    num = random.choice(range_num)
    res_res = num * num

    print(f"Calcule o valor de: {num} x {num}")
    res = int(input("Digite a resposta: "))

    if res == res_res:
        vic.append(1)
        
    return vic


def play():

    plays = 5
    
    for i in range(plays): 

        random.choice(modos)
    
    print(len(vic))
    
    
    
num_0_9 = number_generate(1,10)
num_10_99 = number_generate(10,100)
num_100_999 = number_generate(100,1000)
num_10_999 = number_generate(10,1000)
num_end_5 = number_generate(5,95,10)

modos = [multiply_by_11(num_10_99), square_end_5(num_end_5)]

play()

