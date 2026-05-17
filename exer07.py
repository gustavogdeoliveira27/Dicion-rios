entrada = input("Digite nomes (separados por vírgula): ")
nomes = [nome.strip() for nome in entrada.split(",")]
dados = dict.fromkeys(nomes, 0)

print("Dicionário criado com fromkeys():", dados)