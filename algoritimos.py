import random
# random.randint(min,max)
random.randint(1,10)

v1 = random.randint(1,10)
v2 = random.randint(50,75)

valor = random.randint(10,20)
print("o valor gerado é:",valor)
print("o antecessor é:",valor - 1)
print("o sucessor é:",valor + 1)

valor2 = int(input("digite um valor minimo:"))
valor3 = int(input("digite um valor maximo:"))
valor =random.randint(valor2,valor3)
print("o valor gerado é:",valor)
print("o antecessor é:",valor - 1)
print("o sucessor é:",valor + 1)

