import random


lista_num_2digs = []

for i in range(10,100):

    lista_num_2digs.append(i)

num_1 = random.choice(lista_num_2digs)

conta_11 = f"{num_1} x 11"

res_res = int(num_1) * 11 

while True:
    print(f"Calcule o valor de: {conta_11}")
    res = int(input("Digite a resposta: "))

    if res == res_res:
        print("Resposta correta")
        break
    else:
        print("Resposta errada.")



