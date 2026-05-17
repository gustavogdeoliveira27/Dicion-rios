estoque = {
    "sabonete": 3.50,
    "shampoo": 5.50,
    "condicionador": 4.50
}

produto = input("Digite um nome de produto: ")

if produto in estoque:
    valor = estoque[produto]
    print(f"O valor do produto é R${valor:.2f}")
else:
    print("Produto inexistente")


    

