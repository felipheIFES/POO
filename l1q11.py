print('\n***** Triângulo de Floyd *****')


numero = 1
camada_atual = 1
camada=int(input('Digite um número: '))

while camada_atual <= camada:
    indice = camada_atual
    while indice > 0:
        print(numero, end=" ")
        indice -= 1
        numero += 1
        

    camada_atual += 1
    print('')