import os

tamanho = 0
while(tamanho <= 5):
    usuario = input("informe seu usuario de email: ")
    tamanho = len(usuario)
    if(tamanho <= 5):
        print("informe um email maior que 5 caracters")

print("escolha um dominio")
print("1 - @ifpr.edu.br")
print("2 - @gmail.com")
print("3 - @hotmail.com")
print("4 - outro: ")

dominio = int(input("informe seu dominio escolhido: "))

if(dominio == 1):
    email = usuario + "@ifpr.edu.br"

elif(dominio == 2):
    email = usuario + "@gmail.com"

elif(dominio == 3):
    email = usuario + "@hotmail.com"

else:
    dominio = ""
    while (not("@" in dominio and ".com" in dominio)):
        dominio = input("digite seu dominio de email com @ e com .com: ")

    email = usuario + dominio

print(f"seu email é: {email}")


tamanho = 0
while(tamanho < 10):
    mensagem = input("digite uma mensagem com mais de 10 caracteres:")
    tamanho = len(mensagem)


print("------------------------------------------------------------------------------------------------------------------------")
print("iniciando processo Github")
print("------------------------------------------------------------------------------------------------------------------------")

# executar os comandos do git no terminal

#configurar o email
c = f"git config user.email \"{email}\""
os.system(c)

#identificar as novidades e incluir no commit
# * é identificado como tudo
c = f"git add *"
os.system(c)

#registrar o commit com uma mensagem 
c = f"git commit -m \"{mensagem}\""
os.system(c)

#enviar  para os servidores do github
c = "git push"
os.system(c)

