salarioAtual = float(input('Digite o salário atual de um fincionário: '))
aumento = salarioAtual * 15/100
novoSalario = salarioAtual + aumento
print(f'O novo salário do fincionário com um aumento de 15% é igual a R${novoSalario:.2f}')