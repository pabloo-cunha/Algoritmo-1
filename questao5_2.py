num1 = int(input('Insira um numero a partir do 50 para H: '))
num2 = int(input('Insira um numero a partir do 50 para S: '))
num3 = int(input('Insira um numero a partir do 50 para P: '))

h_1 = ((1*2-1)/1)+((2*2-1)/2)
s_2 = (1/(1*1))-(2/(2*2))
p_3 = 0

countH = 2
countS = 2
y = 1


if num1 >= 50:
    for n in range(2, num1+1):

        if countH % 2 == 0:
            h_1 += (n*2-1)/n
            countH += 1
            
        else:
            h_1 -= (n*2-1)/n
            countH += 1
            
    print(f'O resultado de H é {h_1:.3f}')
    
else:
    print(f'Numero 1 invalido')
    
if num2 >= 50:
    for x in range(2, num2+1):

        if countS % 2 == 0:
            s_2 -= x/(x*x)
            countS += 1
        else:
            s_2 += x/(x*x)
            countS += 1
            
    print(f'O resultado de S é {s_2:.3f}')
else:
    print(f'Numero 2 invalido')

if num3 >= 50:
    for i in range(2, num3+1):
        j = 2
        primo = True
        while j < i:
            if i % j == 0:
                primo = False
                break
            j = j + 1

        if primo:        
            p_3 += i/(y**3)
            y += 2
    
    print(f'O resultado de P é {p_3:.3f}')

else:
    print(f'numero invalido inserido')
