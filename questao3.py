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
    c = c * taxaCrescimentoC
    count += 1
    count2 += 1 

while a < c:
    a = a * taxaCrescimentoA
    c = c * taxaCrescimentoC
    count2 += 1
    if a > c*1.023:
        break

print(f'A população de A ultrapasssará a população de B em {count} anos.')
print(f'A população de A ultrapassará a população de B em {count2} anos.')
        
