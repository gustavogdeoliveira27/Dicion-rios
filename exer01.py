dados = {
    "nome": "Gustavo",
    "idade": 20,
    "cidade": "Curitiba"
}
chave = input("Digite a chave (nome, idade, cidade): ")
if chave in dados:
    print("Valor:", dados[chave])
else:
    print("Chave não encontrada.")

