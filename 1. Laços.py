for numero in range(1, 21):
    if numero != 13:
        print(numero)

####################################

numero = 1
while numero <= 20:
    if numero != 13:
        print(numero)
    numero += 1

#####################################

for numero in range(1, 21):
    if numero == 13:
        continue
    print(numero)
