# vamos usar uma variável chamada nome para
# guardar o nome do cliente. Utilizaremos também
# o comando input(in -> dentro | put -> por em algum lugar )

nome = input("Digite o seu nome:")    # o input faz o printf e o scanf da linguagem C
print("Olá Sr(a)."+nome)                # para pegarmos o nome digitado usamos esse "+" junto com o nome da variável 
print(f"Olá Sr(a). {nome}")             # usamos no inico o "f" de format e usamos a "{}" na variável

# O operador +(mais) foi utilizado para
# concatenar(juntar) o texto entre aspas("")
# com a variável nome 
print("Olá Sr(a)."+nome+". seja bem vindo")
# abaixo, usamos o comando print com a letra
# f(format)
print(f"Olá Sr(a). {nome}, seja bem vindo")