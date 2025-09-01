# Leia uma linha com o número do cartão
numero = input()
lista = [int(digito) for digito in str(numero)]
invertida = lista(::-1)


npi = invertida[1::2]

npp = invertida[::2]
l3 = npi + npp + npp

divisor = 10
if l3 % divisor == 0:
    print("Cartão Válido")
else:
    print("Cartão Inválido")


