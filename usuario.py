"""Como importar Um Modulo, ou Uma Classe:"""

#Modulo
from calculadora import soma, subtrair

#Modulo
from Ola_Mundo import ola_mundo

#Classe:
import classe_calculadora as ca

#Modulo:
x = soma(8, 4)
y = subtrair(8, 9)
print(f"Soma {x}\n"
      f"Subtração {y}")


n = ola_mundo("Diskon")


#Classe:
Calcula = ca.cal(2, 3)
print(Calcula.add())


Calcula = ca.cal(2, 3)
print(Calcula.sub())

