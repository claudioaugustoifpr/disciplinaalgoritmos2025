# tabuada = int(input("digite um numero: "))
# for i in range (1,11):
#     resultado = tabuada * i
#     print(f"{tabuada} x {i} = {resultado}")

numero = int(input("digite um numero: "))
inicio = int(input("digite um numero inicial:"))
fim = int(input("digite um numero final:"))

for i in range (inicio,fim+1):
    print(f"{numero} X {i} = {numero * i}")