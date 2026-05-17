dados = {"Nome": "Gustavo", "Idade": 20, "Cidade": "Curitiba"}
copia = dados.copy()

chave = input("Digite a chave da cópia que deseja alterar (Nome, Idade, Cidade): ")

if chave in copia:
    novo_valor = input("Digite o novo valor: ")
    
    if chave == "idade":
        novo_valor = int(novo_valor)
    copia[chave] = novo_valor
else:
    print("Chave não encontranda.")

print("Original:", dados)
print("Cópia:", copia)

