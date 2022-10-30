# Utilizando o mesmo número inserido para as três equações

num = int(input('Insira um número a partir de 50: '))

h = ((1*2-1)/1)+((2*2-1)/2)
s = (1/(1*1))-(2/(2*2))
p = 0


y = 1
countH = 2
countS = 2
if num >= 50:
    for n in range(2,num+1):
                
        if countH % 2 == 0:
            h += (n*2-1)/n
            countH += 1
        else:
            h -= (n*2-1)/n
            countH += 1
            
    for x in range(2, num+1):
        
        if countS % 2 == 0:
            s -= x/(x*x)
            countS +=1
        else:
            s += x/(x*x)
            countS += 1
            
    for i in range(2, num+1):
            j = 2
            primo = True
            while j < i:
                if i % j == 0:
                    primo = False
                    break
                j = j + 1

            if primo:        
                p += i/(y**3)
                y += 2
        
            
    print (f'O resultado de H é {h:.3f}')
    print (f'O resultado de S é {s:.3f}')
    print (f'O resultado de P é {p:.3f}')
    
else:
    print('Número inserido é invalido!')
