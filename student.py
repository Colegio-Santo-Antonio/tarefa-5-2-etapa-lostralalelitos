numero = input()
lista = [int(digito) for digito in numero]
invertida = lista[::-1]

npi = invertida[1::2]  
npp = invertida[::2]   

npp_corrigido = []
for a in npp:
    dobro = a * 2
    if dobro > 9:
        dobro -= 9
    npp_corrigido.append(dobro)

p = sum(npi) + sum(npp_corrigido)

if p % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")


# Feito por Mateus Loures, Davi Versiani e João Vitor Toscano do 1ºF
