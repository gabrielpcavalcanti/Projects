import random

words = {"conheciemento": "knowledge", "crença": "belief", "sociedade": "society"}

chave_aleatoria = random.choice(list(words.keys()))

print(f"Palavra: {chave_aleatoria}")

resp = input("Digite a resposta: ").lower()
check = words[chave_aleatoria]

if resp == check:
    print("Correto")
else:
    print("Errado")



