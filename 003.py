cardapio = {
    "Pizza": 10,
    "Suco": 5,
    "Bolo": 7,
    "Refrigerante": 8
}

itens = list(cardapio.keys())
preco_total = 0

for i in range(len(itens)):
    item = itens[i]
    preco = cardapio[item]
    preco_total += preco
    # i + 1 exibe o índice começando de 1 até 4
    print(f"Item {i + 1} - {item}: R$ {preco}")

print(f"\nTotal: R$ {preco_total}")