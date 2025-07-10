largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
qtdLitrosDeTinta = area / 2
print(f'A área da parede é {area}m2') 
print(f'Será necessário {qtdLitrosDeTinta}l de tinta para pintar a a parede')