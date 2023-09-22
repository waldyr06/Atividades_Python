import time
def contagem_regressiva (i:int):
    if(i <= 0): print(0)
    else:
        time.sleep(1)
        print (i)
        return contagem_regressiva(i-1)
print (f"A Contagem Regressiva de 10:")
contagem_regressiva(10)

def soma_recursiva(i:int):
    if(i <= 1): return 1
    else:
        time.sleep(0.5)
        return i + soma_recursiva(i-1)
print("Soma Recursiva:")
print(f"De 2: {soma_recursiva(2)}")
print(f"De 3: {soma_recursiva(3)}")
print(f"De 4: {soma_recursiva(4)}")
print(f"De 5: {soma_recursiva(5)}")
print(f"De 8: {soma_recursiva(8)}")
print(f"De 9: {soma_recursiva(9)}")
print(f"De 11: {soma_recursiva(11)}")

time.sleep(1)
def potencia(base, expoente):
    if expoente == 0: return 1
    else: 
        time.sleep(0.5) 
        return base * potencia(base, expoente - 1)
print (f"5 elevado a 5: {potencia(5, 5)}")
print (f"7 elevado a 4:  {potencia(7, 4)}")
print (f" 9 elevado a 2: {potencia(9, 2)}")
print (f" 9 elevado a 5:  {potencia(9, 5)}")

def inverter_string(s):
    if len(s) == 0: return ""
    else: 
        time.sleep(0.5) 
        return s[-1] + inverter_string(s[:-1])
print(inverter_string("alta"))
print(inverter_string("novamente"))
print(inverter_string("savana"))
print(inverter_string("givanio é legal"))
print(inverter_string("vitor coçante"))
