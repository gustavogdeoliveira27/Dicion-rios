dados = {
    "nome": "Gustavo",
    "sobrenome": "Oliveira",
    "curso": "Engenharia de Software"
}
print("Primeiro dicionário:", dados)

chave = input("Digite uma chave para remover: ")
if chave in dados:
    dados.pop(chave)
    print("Depois do pop():", dados)
else:
    print("Chave não encontrada.")

if dados:
    removido = dados.popitem()
    print("Item removido com popitem(): ", removido)
    print("Deppois do popitem():", dados)

nova_chave = input("Digite uma nova chave: ")
novo_valor = input("Digite o valor: ")

dados.update({nova_chave: novo_valor})
print("Dicionário final:", dados)



nova_chave = input("Nova chave para adicionar via update(): ")
novo_valor = int(input("Novo valor: "))
dados.update({nova_chave: novo_valor})

print("Dicionário final:", dados)