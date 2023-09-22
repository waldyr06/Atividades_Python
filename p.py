with open("alunos.txt", "w") as arquivo:
    arquivo.write("waldyr, 10\n")
    arquivo.write("waldyr, 10\n")
    arquivo.write("waldyr, 10\n")
    arquivo.write("waldyr, 10\n")
    arquivo.write("waldyr, 10\n")
    arquivo.write("waldyr, 10\n")
    arquivo.write("eu, 3\n")

notas = []
aprovados = [] 
reprovados = []

with open("alunos.txt", "rt") as arquivo:
    with open("aprovados.txt", "w") as aprovados_arquivo, open("reprovados.txt", "w") as reprovados_arquivo:
        for arquivo in arquivo:
            arquivo = arquivo.split(":")[0]
            nota = 0
            if len(arquivo.split(":")) >= 2:
                nota = int(arquivo.split(":")[1])
            if nota >= 6:
                aprovados_arquivo.write(f"{arquivo}\n")
            else:
                reprovados_arquivo.write(f"{arquivo}\n")
            
        
