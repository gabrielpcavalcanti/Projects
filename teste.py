import random

lista_materias = ['Ciências', 'Geografia', 'Filosofia', 'Psicologia', 'História', 'Arte']


for i in range(5):
    print(random.sample(lista_materias, 2))

#print(help(random))