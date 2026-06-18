import time, os, sys            #importação de módulos

os.system("cls")

print(time.time())

i = 0 

while i <= 10000:
    i+=1

print(time.time())                  # aparentemente mostra o tempo que levou para processar os comandos
sys.stdout.write("Mensagem")
