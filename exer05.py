dados = {"nome": "Gustavo", "Idade": 20, "Cidade": "Curitiba"}
print("Dicionário atual: ", dados)

resposta = input("Deseja apagar todos os dados? Digite sim ou não: ")
if resposta == "sim":
    dados.clear()
    print("Dados apagados")
else:
    print("Dicionário final:", dados)
