# Leia uma linha com o número do cartão
numero = input()
lista = [int(digito) for digito in numero]
invertida = lista(::-1)


npi = invertida[1::2]

npp = invertida[::2]

a = sum(npi) + sum(npp) + sum(npp)

divisor = 10
if a % divisor == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")


