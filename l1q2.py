minu=0
segu=0
hora=0

print('\n\n*****  CONVERSOR: SEGUNDOS => H:MIN:SEG  *****')
tempo=int(input('\n       Digite o tempo em segundos: '))
while tempo > 59:
    minu += 1
    tempo = tempo - 60
    if tempo < 60:
        segu = tempo

while minu > 59:
    hora += 1
    minu = minu - 60
    
print('\n       Resultado (H:MIN:SEG) = ' ,hora,':',minu,':',segu)