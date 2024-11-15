
list= []
contador_mensaje = 0
for i in range(4):
    if contador_mensaje == 0:
        valor = int(input("Ingrese el valor de A: "))
        A = valor
    elif contador_mensaje == 1:
        valor = int(input("Ingrese el valor de B: "))
        B = valor
    elif contador_mensaje == 2:
        valor = int(input("Ingrese el valor de C: "))
        C = valor
    elif contador_mensaje == 3:
        valor = int(input("Ingrese el valor de D: "))
        D = valor
    else:
        print("ALGO SALIO MAL")
    list.append(valor)
    contador_mensaje += 1

#Acomodar las lista tanto de forma ordenada como inversa
lista_orden = sorted(list)
lista_orden_inverso = sorted(list, reverse=True)

#Mostrar la informacion
print(f"Los valores ingresados fueron A={A}. B={B}, C={C}, D={D}.")
print(f"Los valores en orden se veria de esta forma {lista_orden[:]}")
print(f"Los valores en orden inverso se veria de esta forma {lista_orden_inverso[:]}")
