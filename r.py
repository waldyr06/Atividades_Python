a_contatos = open("contatos.txt", "w")

l_contatos = []

def abrir_agenda():
    with open(a_contatos, "r") as arquivo:
        return arquivo.read().split()

def salvar_agenda():
    with open(a_contatos, "w") as arquivo2:
        return arquivo2.write("/n".join(l_contatos))

def criar_contato():
    global nome, end, tel, tipo
    nome = input("Digite o nome do contato: ")
    end = input("Digite o endereço do contato: ")
    tel = input("Digite o número telefone do contato: ")
    tipo = input("Selecione o tipo desse contato (Pessoal, Profissional, Romantico): ")
    
    contato = f"Nome: {nome}  |  Endereço: {end}  |  Telefone: {tel}  |  Tipo: {tipo}\n"
    l_contatos.append(contato)
    print("O contato foi criado!")

def edit_contato():
    nome = input("Digite o nome do contato que deseja alterar: ")
    global end, tel, tipo
    contato_encontrado = False 
    
    for i, contato in enumerate():
        if f"Nome: {nome}" in contato: 
            print("Detalhes do contato atual:")
            print(contato)
            opcao = input("""1. Nome | 2. Endereço | 3. Telefone | 4. Tipo | 5. Retornar
            Selecione o que deseja alterar: """)
            if opcao == "1": 
                nome = input("Digite o novo nome do contato: ")
                # Atualize o nome no contato atual
                contato = f"Nome: {nome}  |  Endereço: {end}  |  Telefone: {tel}  |  Tipo: {tipo}"
            elif opcao == "2":
                end = input("Digite o novo endereço do contato: ")
                # Atualize o endereço no contato atual
                contato = f"Nome: {nome}  |  Endereço: {end}  |  Telefone: {tel}  |  Tipo: {tipo}"
            elif opcao == "3":
                tel = input("Digite o novo número de telefone do contato: ")
                # Atualize o telefone no contato atual
                contato = f"Nome: {nome}  |  Endereço: {end}  |  Telefone: {tel}  |  Tipo: {tipo}"
            elif opcao == "4":
                tipo = input("Selecione o novo tipo desse contato (pessoal, profissional, romantico): ")
                # Atualize o tipo no contato atual
                contato = f"Nome: {nome}  |  Endereço: {end}  |  Telefone: {tel}  |  Tipo: {tipo}"
            elif opcao == "5":
                return
        
    if not contato_encontrado:
        print("Contato não encontrado!")

    print("Contato alterado!")

def remov_contato():
    nome = input("Digite o nome do contato que deseja apagar: ")
    for i in l_contatos:
        contato = l_contatos
        if f"Nome: {nome}" in l_contatos:
            print("Detalhes do contato: ")
            print(nome)
            opcao = input("""Deseja realmente apagar esse contato?
            1. Sim  |  2. Não
            Digite o número correspondente à ação: """)
            if opcao == "1": 
                l_contatos.pop(i)
                print("Contato Apagado!")
            elif opcao == "2":
                print("Contato não Apagado!")
                return
        else: 
            print("Contato não Encontrado!")
            continue

def list_contato(l_contatos):
    if not l_contatos:
        print("A lista de contatos está vazia!")
    else:
        print("\nLista de Contatos:")
        for contato in l_contatos:
            print(contato)
            print("--------------------")
        opcao = input("""Deseja sair da lista? (S/N)
        """).strip().lower()
        if opcao == "s":
            return
        else:
            list_contato(l_contatos)

def main():
    global l_contatos

    while True:
        print("Menu Principal:")
        print("1. Criar Contato | 2. Editar Contato | 3. Apagar Contato | 4. Listar Contatos | 5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            criar_contato()
        elif opcao == "2":
            edit_contato()
        elif opcao == "3":
            remov_contato()
        elif opcao == "4":
            list_contato(l_contatos)
        elif opcao == "5":
            while True:
                r = input("Deseja salvar a agenda antes de sair? (S/N): ").strip().lower()
                if r == "s":
                    salvar_agenda()
                    print("A sua agenda foi salva!")
                    print("Saindo do Programa...")
                    break
                elif r == "n":
                    print("Saindo do Programa...")
                    break
                else:
                    print("""Resposta Inválida
                    Digite 'S' para Salvar e 'N' para Não Salvar""")
                    break
        else:
            print("Opção Inválida, Tente Novamente!")
            return opcao

if __name__ == "__main__":
    main()
                                

print(main)