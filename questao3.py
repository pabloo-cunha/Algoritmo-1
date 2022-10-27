a = 15000
b = 45000
c = 65000

taxaCrescimentoA = 1.1
taxaCrescimentoB = 1.05
taxaCrescimentoC = 1.025

count = 0
count2 = 0
while a < b:
    a = a * taxaCrescimentoA
    b = b * taxaCrescimentoB

    count += 1
    

a = 15000

while a < c*1.23:
        a *= taxaCrescimentoA
        c *= taxaCrescimentoC  
              
        count2 += 1
        
print(f'A população de A ultrapasssará a população de B em {count} anos.')
print(f'A população de A ultrapassará a população de C em {count2} anos.')

