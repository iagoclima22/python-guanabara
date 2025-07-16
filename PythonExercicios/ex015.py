dias_alugados = int(input("Quantos dias alugados? "))
distancia_percorrida = float(input("Quantos Km rodados? "))
preco_a_pagar = (60 * dias_alugados) + (0.15 * distancia_percorrida)
print("O total a pagar é R${:.2f}".format(preco_a_pagar))
