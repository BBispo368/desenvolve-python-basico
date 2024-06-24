lista1 = [i for i in range(20,51) if i%2==0]
print(lista1)

#--------------------------------------------#

lista = [1,2,3,4,5,6,7,8,9]
lista2 = [i**2 for i in lista]
print(lista2)

#--------------------------------------------#

lista3 = [i for i in range(1,100) if i%7==0]
print(lista3)

#--------------------------------------------#

lista4 = ["Par" if i%2==0 else "Impar" for i in range(0,30,3)]
print(lista4)