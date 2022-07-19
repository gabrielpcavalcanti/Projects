lista_num =[]
lista_num_impar = []
lista_num_b = []
lista_num_c = []
lista_num_final = []

for i in range(100,1000):
    lista_num.append(i)

#print(lista_num)

for k in lista_num:

    if k % 2 != 0:
        lista_num_impar.append(k)
        continue
    else:
        continue

#print(lista_num_impar)

for l in lista_num_impar:

    if l % 5 == 3:
        lista_num_b.append(l)
        continue
    else:
        continue

print(lista_num_b)

for n in lista_num_b:

    if n % 7 == 5:
        lista_num_c.append(n)
        continue
    else:
        continue

print(lista_num_c)

for x in lista_num_c:

    if x % 9 == 1:
        lista_num_final.append(x)
        continue
    else:
        continue

print(lista_num_final)
