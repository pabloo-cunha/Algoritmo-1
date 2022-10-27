salarioFixo = int(input('Salario do funcionario: '))
vendas = int(input('Valor da vendas: '))

if vendas <= 1500:
    bonus5 = vendas * 0.05
    salarioTotal = bonus5 + salarioFixo

    print(f'O salario total será de {salarioTotal} Reais')

if vendas > 1500:
    bonus5 = 1500 * 0.05
    bonus7 = (vendas - 1500) * 0.07
    salarioTotal = bonus5 + bonus7 + salarioFixo
    
    print(f'O salario total será de {salarioTotal} Reais')