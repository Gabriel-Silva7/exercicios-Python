# vamos usar uma variável chamada nome para
# guardar o nome do cliente. Utilizaremos também
# o comando input(in -> dentro | put -> por em algum lugar )

nome = input("Digite o seu nome:")    # o input faz o printf e o scanf da linguagem C
print("Olá Sr(a)."+nome)                # para pegarmos o nome digitado usamos esse "+" junto com o nome da variável 
print(f"Olá Sr(a). {nome}")             # esse com a "{}" funciona da mesma maneira 


print("Olá Sr(a)."+nome+". seja bem vindo")                
print(f"Olá Sr(a). {nome}, seja bem vindo")