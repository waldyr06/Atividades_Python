import time
x = 0
a = input("Digite o nome do Professor de Desenvolvimento de Sistemas: ")
a1 = a.lower()
time.sleep (2)
if (a1 == "givanio"):
    x = x + 1
    print("Parabéns! Você acertou o Nome do Professor")
else:
    input("Está errado, aperte Enter para a Próxima pergunta... ")
time.sleep (2)
print("------------------------------------------------------------------------------")
b = input("Qual a cor Favorita de Christian?: ")
b1 = b.lower()
time.sleep (2)
if (b1 == "preto"):
    x = x + 1
    print("Parabéns! Você acertou")
else:
    input("Está errado, aperte Enter para a Próxima pergunta... ")
time.sleep (2)
print("------------------------------------------------------------------------------")
c = input("No 2°B não existe?: ")
c1 = c.lower()
time.sleep (2)
if (c1 == "medo"):
    x = x + 1
    print("Parabéns! Você acertou")
else:
    input("Está errado, aperte Enter para a Próxima pergunta... ")
time.sleep (2)
print("------------------------------------------------------------------------------")
d = input("Qual a cor favorita de waldyr?: ")
d1 = d.lower()
time.sleep (2)
if (d1 == "azul"):
    x = x + 1
    print("Parabéns! Você acertou")
else:
    input("Está errado, aperte Enter para a Próxima pergunta... ")
time.sleep (2)
print("------------------------------------------------------------------------------")
e = input("Givanio tem quantos anos?: ")
time.sleep (2)
if (e == "18" or e=="19"):
    x = x + 1 
    print("Parabéns! Você acertou")
else:
    input("Está errado, aperte Enter para a Próxima pergunta... ")
time.sleep (2)
print("------------------------------------------------------------------------------")
f = input("Marques é Judeu? (S/N): ")
f1 = f.lower()
time.sleep (2)
if (f1 == "s"):
    x = x + 1
    print("Parabéns! Você acertou")
else:
    input("""Está errado, esse assunto não tem discussão, ele é Judeu e PRONTO. 
    Pressione Enter para a próxima pergunta. """)
time.sleep (2)
print("------------------------------------------------------------------------------")
g = input("Qual a tradução de (Sun): ")
time.sleep (2)
g1 = g.lower()
if (g1 == "sol"):
    x + x + 1 
    print("Parabéns! Você acertou")
else:
    input("Está errado, aperte Enter para a Próxima pergunta... ")  
time.sleep (2)
print("------------------------------------------------------------------------------")
h = input("Qual a melhor cor da camisa do interclasse (Branca ou Preta): ")
time.sleep (2)
h1 = h.lower()
if (h1 == "branca"):
    x = x + 1
    print("Parabéns! Você acertou")
else:
    print("Melhore seu gosto (brincadeira) ")
time.sleep (2)
print("------------------------------------------------------------------------------")
i = input("No zoológico tem?: ")
time.sleep (2)
i1 = i.lower()
if (i1 == "animais"):
    x = x + 1
    print("Parabéns! Você acertou")
else:
    input("Está errado, aperte Enter para a Próxima pergunta... ")
time.sleep (2)
print("------------------------------------------------------------------------------")
j = input("O corinthians é o melhor (S/N)")
j1 = j.lower()
time.sleep (2)
if (j1 == "S"):
    x = x + 1
    print("Parabéns! você acertou")
else:
    print("É claro que o Timão é o melhor")
time.sleep (2)     
print("------------------------------------------------------------------------------")
input("Aperte Enter e descubra sua nota")
time.slee1 (2)
print(f"Sua nota foi {x}/10")