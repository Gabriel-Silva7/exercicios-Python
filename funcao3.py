# importação de funções especificas do módulos.
# o comando from(origem) que indica de onde vem as funções.
# ou seja, de qual módulo você esta extraindo as funçoes 
# o comando import, indica quais funções você irá usar do(from)
# módulo carregado pelo comando from(origem) 

from os import system, cpu_count
from math import sqrt, pow, pi
system("cls")        # para ver as funções do "import" CRTL + espaço, você consegue ver as funções do "import"
print(cpu_count())   # mostras a quantidade de cpu
print("========== Origem math ===========")
print(sqrt(49))
print(pow(2,5)) 
     