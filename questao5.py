num = int(input('Insira um numero a partir do 50: '))

h = ((1*2-1)/1)+((2*2-1)/2)
s = (1/(1*1))-(2/(2*2))

countH = 2
countS = 2

for n in range(2,num):
              
    if countH % 2 == 0:
        h += (n*2-1)/n
        countH += 1
    else:
        h -= (n*2-1)/n
        countH += 1
        
for x in range(2, num):
    
    if countS % 2 == 0:
        s -= x/(x*x)
        countS +=1
    else:
        s += x/(x*x)
        countS += 1
        
print (f'O resultado de H é {h:.2f}')
print (f'O resultado de S é {s:.2f}')
# print (f'O resultado de P é {}')