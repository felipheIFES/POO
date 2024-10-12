print('\n***** n-ésimo termo da sequência *****')

n=int(input('\nDigite um número: '))

n1 = 1
n2 = 1
total = 0

while n1 <= n:
    total += n1
    n1 += 1

print('\n', total, '(', end=" ")

while n2 < n:
    print(n2, end=" + ")
    n2 += 1

print(n2, ')')
print('')