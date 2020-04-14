def aumento(salario):
    porc = 0.15
    novoSalario = salario + (salario * porc)
    return ('=' * 24 +f'\nSalário Atual R${salario:.2f}\n{porc * 100}% de aumento\nSalário com Aumento\nR${novoSalario:.2f}\n'+'=' * 24)


salario = float(input('Qual o salário atual.: '))
print(aumento(salario))