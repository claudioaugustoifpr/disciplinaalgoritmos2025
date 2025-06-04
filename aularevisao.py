# import random

# pc = random.randint(1,3)
# user = int(input("""\n faça uma jogada entre:===\n1.pedra\n2.papel\n3.tesoura\n===\n\n"""))

# if(user == 1 ):
#     if(pc == 1):
#         print("empate")
#     elif(pc == 2):
#         print("pc ganhou")
#     elif(pc == 3):
#         print("voce venceu")

# elif(user == 2):
#     if(pc == 2):
#         print("empate")

#     elif(pc == 1):
#         print("voce ganhou")
#     elif(pc == 3):
#         print("pc venceu")

# elif(user == 3):
#     if(pc == 3):
#         print("empate")
#     elif(pc == 2):
#         print("voce venceu")
#     elif(pc == 1):
#         print("pc venceu")


# else:
#     print("valor invalido")

# #========================================================================
# import random

# nota1 = int(input("digite a primeira nota:"))

# nota2 = int(input("digite a segunda nota:"))

# nota3 = int(input("digite a terceira nota:"))



# media = (nota1 + nota2 + nota3) / 3

# conceitofinal = ""

# if(media >= 90 ):
#     conceitofinal = "A"
# elif(media >= 75 and media <= 89):
#     conceitofinal = "B"
# elif(media >= 55 and media <= 74):
#     conceitofinal = "C"
# else:
#     conceitofinal = "D"
    

# print(f"o conceito final é {conceitofinal} ")
#=================================================================================

# print("inicio do programa")
# cont = 1
# while(cont < 6):
#     print("valor de cont",cont)
#     cont += 1
# print("fim do algoritmo")


# entrada = 0
# while(entrada != 3):
#     print("menu de opçoes: \n1.cadastrar \n2.alterar \n3.sair")
#     entrada = int(input("digite uma opçao"))

# print("fim do programa")

#============================================================================#

# num = 1
# soma = 0
# while(num <= 10):
#     if(num % 2 == 0):
#         print(num)
#     soma = soma + num
#     num = num + 1
# print(soma)

# total = 0
# num = 1

# while(num <= 10):
#     if(num % 2 == 0):
#         print(num)
#         total = num + total
#     num = num + 1
# print(total)

# num = int(input("digite um numero: "))

# while(num != 8):
#     num = int(input("digite outro numero: "))
# print("fim do programa")

# import random

# n = 1
# m = 0
# while(n != 3):
#     m = random.randint(1,10)
#     if(m == 3):
#         print("fim do programa")
#         break
#     print(m)

# import random

# n = random.randint(1,10)

# while(n != 3):
#     print(n)
#     n = random.randint(1,10)

# paranavai = 95500
# maringa = 409000

# anos = 0
# while(paranavai < maringa):
#     paranavai += paranavai * 0.05
#     maringa += maringa * 0.02
#     anos += 1
# print(f"levara {anos}")