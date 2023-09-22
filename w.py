def cal():
    a = float(input("Digite sua Altura (m): "))
    b = float(input("Digite seu Peso (kg): "))
    imc = b / a**a
    print("--------------------------------------")
    print(f"Seu IMC é: {imc:.1f}")
    print("--------------------------------------")
    if imc < 16.9:
        print("Você está MUITO Abaixo do Peso")
    elif imc >= 17 and imc <= 18.4:
        print("Você está Abaixo do Peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Você está em um Peso Normal")
    elif imc >= 26 and imc <= 29.9:
        print("Você está Acima do Peso")
    elif imc >= 30 and imc <= 34.9:
        print("Você está com Obesidade de Grau I")
    elif imc >= 35 and imc <= 40:
        print("Você está com Obesidade de Grau II")
    elif imc > 40:
        print("Você está com Obesidade de Grau III")
    else:
        print("Tente Novamente")
        return
    print("--------------------------------------")

cal()


