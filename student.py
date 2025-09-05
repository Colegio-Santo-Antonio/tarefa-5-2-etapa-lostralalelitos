numero = input()
lista = [int(digito) for digito in numero]
invertida = lista[::-1]

npi = invertida[1::2]
npp = invertida[::2]


npp = [a*2 if a*2 <= 9 else a*2 - 9 for a in npp]

p = sum(npi) + sum(npp)

if p % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")

# Feito por Mateus Loures do 1ºF
