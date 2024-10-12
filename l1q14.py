print('\n***** A série de Madhava *****')

n=int(input('\nDigite um número: '))

i = 0
res = 0

while i <= n:
    num = (-1)**i

    den = (2*i + 1)*(3**i)
    
    aux = num / den

    res += aux

    i += 1

S = (12**0.5) * res

print('\nPara n igual a', n, ', o valor de pi é', S)
print('')