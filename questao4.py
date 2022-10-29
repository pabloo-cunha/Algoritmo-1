from random import randint        

ultimo_num = None


soma1 = 0
contador1 = 1
maior_soma1 = 0
maior_sequencia1 = 0


maior2 = None
contador2 = 1
maior_soma2 = 0
maior_sequencia2 = 0
      

for n in range(0, 150):
    entrada = randint(0, 10)

    if ultimo_num and ultimo_num == entrada - 1:            
        soma1 += entrada
        contador1 += 1
        contador2 = 1

        if (contador1 == maior_sequencia1 and soma1 > maior_soma1) or contador1 > maior_sequencia1:
            maior_soma1 = soma1
            maior_sequencia1 = contador1

    elif ultimo_num and ultimo_num == entrada:
        contador1 = 1
        soma1 = entrada
        contador2 += 1

        if contador2 > maior_sequencia2 or (contador2 == maior_sequencia2 and entrada > maior2):
            maior2 = entrada
            maior_sequencia2 = contador2


    else:
        contador1 = 1
        soma1 = entrada
        contador2 = 1
        

    ultimo_num = entrada


if maior_sequencia1 != 0:
    print(f"Maior sequencia consecutiva de números em ordem crescente: {maior_sequencia1}. A maior soma é: {maior_soma1}")

else:
    print("Não houve sequência númerica")

if maior2 and maior_sequencia2 != 0:
    print(f"Maior sequencia consecutiva de números constantes: {maior_sequencia2}. O maior valor constante é:  {maior2}")

else:
    print("Não houve sequência númerica")
