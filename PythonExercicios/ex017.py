from math import hypot

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print("O comprimento da hipotenusa deste triângulo é {}.".format(hipotenusa))