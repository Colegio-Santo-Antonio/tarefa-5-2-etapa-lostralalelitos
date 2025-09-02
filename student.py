# Leia uma linha com o número do cartão
numero = input()
lista = [int(digito) for digito in numero]
invertida = lista[::-1]


npi = invertida[1::2]

npp = invertida[::2]
npp = [a*2 for a in npp]


for i in npp:
    if 10 <= i and i <= 18:
        i = str(i)
        i = sum([int(n) for n in i])
    else:
        i = i

a = sum(npi) + sum(npp)

divisor = 10
if a % divisor == 0:
    print("Cartão inválido")
else:
    print("Cartão válido")


