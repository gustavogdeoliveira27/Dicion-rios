def mostrar_menu():
    print("\n--- MENU ---")
    print("1 - Exibir usuários")
    print("2 - Buscar usuários")
    print("3 - Adicionar usuários")
    print("4 - Atualizar idade")
    print("5 - Remover usuário (pop)")
    print("6 - Remover último (popitem)")
    print("7 - Copiar dicionário e alterar cópia")
    print("8 - Criar com fromkeys")
    print("9 - Atualizar com outro dicionário")
    print("10 - Limpar tudo (clear)")
    print("0 - Sair")


usuarios = {
    "Gustavo": 20,
    "Leticia": 20,
    "Alice": 8
}

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nNomes:", list(usuarios.keys()))
        print("Idades:", list(usuarios.values()))
        print("Completo:", list(usuarios.items()))

    elif opcao == "2":
        nome = input("Nome do usuário: ")
        idade = usuarios.get(nome)

        if idade is None:
            print("Usuário não encontrado.")
        else:
            print(f"{nome} tem {idade} anos.")

    elif opcao == "3":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        usuarios[nome] = idade
        print("Usuário adicionado.")

    elif opcao == "4":
        nome = input("Nome: ")

        if nome in usuarios:
            nova_idade = int(input("Nova idade: "))
            usuarios[nome] = nova_idade
            print("Idade atualizada.")
        else:
            print("Usuário não encontrado.")

    elif opcao == "5":
        nome = input("Nome para remover: ")

        if nome in usuarios:
            usuarios.pop(nome)
            print("Removido.")
        else:
            print("Usuário não existe.")

    elif opcao == "6":
        if usuarios:
            removido = usuarios.popitem()
            print("Removido:", removido)
        else:
            print("Dicionário vazio.")

    elif opcao == "7":
        copia = usuarios.copy()

        nome = input("Nome para alterar na cópia: ")

        if nome in copia:
            copia[nome] = int(input("Nova idade: "))

        print("Original:", usuarios)
        print("Cópia:", copia)

    elif opcao == "8":
        nomes = input("Digite nomes separados por vírgula: ").split(",")

        idade_padrao = int(input("Idade padrão: "))

        novo = dict.fromkeys(
            [n.strip() for n in nomes],
            idade_padrao
        )

        print("Novo dicionário:", novo)

    elif opcao == "9":
        print("Criando novo dicionário...")

        nome = input("Nome: ")
        idade = int(input("Idade: "))

        outro = {nome: idade}

        usuarios.update(outro)

        print("Atualizado:", usuarios)

    elif opcao == "10":
        confirm = input("Tem certeza? (sim/não): ")

        if confirm.lower() == "sim":
            usuarios.clear()
            print("Todos os dados foram apagados.")
        else:
            print("Operação cancelada.")

    elif opcao == "0":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida.")

                
