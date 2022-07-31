"""
Jogo para escolher uma palavra secreta e outra pessoa tenta acerta-la, escolhendo letra por letra.
"""
print("                    Jogo de adivinhar a palavra".upper())
print()
print("Funcionamento: Uma pessoa escolhe um palavra para a outra tentar advinhar.\nA segunda pessoa irá escolher letras"
      " para tentar acertar a palavra.\nEla terá uma quantidade de tentativas que a primeira pessoa escolher. ")
print("-------------------------------------//-------------------------------------")

palavra_secreta = str(input("Digite a palavra secreta: "))
tentativas = int(input("Quantidades de tentativas que a pessoa tem para acertar: "))
resposta = []

print()

while True:

    if tentativas <= 0:
        print("Você Perdeu!!!")
        break

    letra = str(input("Digite uma letra: "))

    if len(letra) > 1:
        print("Não pode ter mais que uma letra.")
        print()
        continue

    resposta.append(letra)

    if letra in palavra_secreta:
        print(f"A letra {letra} está na palavra secreta")
    else:
        print("Essa letra não pertence a palavra secreta")
        resposta.pop()

    resposta_temporaria = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in resposta:
            resposta_temporaria += letra_secreta
        else:
            resposta_temporaria += '*'

    if resposta_temporaria == palavra_secreta:
        print(f"Parabéns, você ganhou!!! \nA palavra era: {palavra_secreta}")
        break
    else:
        print(f"A palavra secreta está assim: {resposta_temporaria}")

    if letra not in palavra_secreta:
        tentativas -=1

    print(f"Ainda tem {tentativas} tentativas.")
