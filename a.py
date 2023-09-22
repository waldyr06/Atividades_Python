import random
print("Roleta russa criada por Christian e Waldyr, se errar pode ter certeza que estaremos atrás de você, te observando hahaha")
while True:
    numero_secreto = random.randint(1, 7)
    while True:
        palpite =int(input("Adivinhe o Número: "))
        if palpite != numero_secreto:
            print("Tente outro número.")
        else:
            print(f"Parabéns, você acertou o número.")
            break