cardapio = ["pastel", "coxinha", "suco"]

cardapio.append("lasanha")

pedido = input('Qual seu pedido? ').strip().lower()

if pedido not in cardapio:
    print("Desculpe, este item não está no cardápio.")
else:
    print(f"Pedido confirmado: {pedido}!")
    print(cardapio)
