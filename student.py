numero = input()
im = [int(i) for i in numero[-1::2]] 
pa = []
for i in numero[=2::2]:
    z = int(i)
    if 2*z < 10:
        pa.append(2*z)
    else:
        pa.append(2*z - 9)

soma = sum(pa) + sum(im)
if soma % 10 ==0:
    print("Cartão válido")
else:
    print("Cartão inválido")

# Feito por Mateus Loures, Davi Versiani e João Vitor Toscano do 1ºF
