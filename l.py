perguntas = ["Que dia é hoje?", "Qual o nome de quem fez essa pergunta?", "Estamos em que mês?", "Quem descobriu o Brasil", "Qual a cor da minha pulseira", "Qual a fruta mais saudavel do mundo", "O orgulho de ser sesi foi bom (S/N)"]
respostas = ["quinta", "waldyr", "agosto", "cabral", "preta", "limão", "n"]
x = 0
for i in range(7):
    pergunta = perguntas[i]
    resposta_certa = respostas[i]
    
    resposta = input(perguntas[i])
    if resposta == resposta_certa:
        x = x + 1
        print("CORRETO")
    else:
        print("incorreto")
print(f"Sua nota foi {x}/7")
if x <=2:
    print("MUITO BURRO KKKKKKKKKKKKKK")
elif x > 2 < 6:
    print("parabéns")