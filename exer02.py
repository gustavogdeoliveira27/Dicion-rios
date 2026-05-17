produtos = {
    "arroz": 20.0,
    "feijao": 8.5,
    "macarrao": 5.0
}
print("Profutos disponíveis:", produtos)
produto = input("Qual produto deseja alterar? ")

if produto in produtos:
    novo_preco = float(input("Digite o novo preço: "))
    produtos[produto] = novo_preco
    print("Dicionário atualizado:", produtos)
else:
    print("Produto não encontrado.")