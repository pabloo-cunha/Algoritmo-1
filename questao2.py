salarioFixo = int(input('Salário do funcionário: '))
vendas = int(input('Valor das vendas: '))

if vendas <= 1500:
    bonus5 = vendas * 0.05
    salarioTotal = bonus5 + salarioFixo

    print(f'O salário total será de {salarioTotal} reais')

if vendas > 1500:
    bonus5 = 1500 * 0.05
    bonus7 = (vendas - 1500) * 0.07
    salarioTotal = bonus5 + bonus7 + salarioFixo
    
    print(f'O salário total será de {salarioTotal} reais')
