
#Ingreso de valores
A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))
C = int(input("Ingrese el valor de C: "))
D = int(input("Ingrese el valor de D: "))
#Agregar los valores a una lista
l = []
l.append(A)
l.append(B)
l.append(C)
l.append(D)
#Acomodar las lista tanto de forma ordenada como inversa
lista_orden = sorted(l)
lista_orden_inverso = sorted(l, reverse=True)
#Mostrar la informacion
print(f"Los valores ingresados fueron A={A}. B={B}, C={C}, D={D}.")
print(f"Los valores en orden se veria de esta forma {lista_orden[:]}")
print(f"Los valores en orden inverso se veria de esta forma {lista_orden_inverso[:]}")
