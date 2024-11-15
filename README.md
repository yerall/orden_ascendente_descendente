# Descripción

Este programa en Python permite ingresar cuatro números enteros, correspondientes a las variables **A**, **B**, **C**, y **D**, y luego los imprime tanto en orden ascendente como descendente. Se presentan tres versiones diferentes del código que producen el mismo resultado.

# Código

## Versión #1

Esta versión utiliza una lista de comprensión para capturar los valores ingresados y luego aplica las funciones de ordenamiento `sorted()` y `sorted(reverse=True)`.

```python
# Ingreso de valores y creación de la lista
valores = [int(input(f"Ingrese el valor de {var}: ")) for var in ["A", "B", "C", "D"]]

# Ordenar la lista en orden ascendente y descendente
lista_orden = sorted(valores)
lista_orden_inverso = sorted(valores, reverse=True)

# Mostrar la información
print(f"Los valores ingresados fueron: A={valores[0]}, B={valores[1]}, C={valores[2]}, D={valores[3]}.")
print(f"Los valores en orden ascendente son: {lista_orden}")
print(f"Los valores en orden descendente son: {lista_orden_inverso}")
```

## Versión #2

En esta versión, cada variable se guarda en una lista usando el método `append()`. Luego, la lista se ordena en ambos sentidos.

```python
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
```

## Versión #3

Esta versión utiliza un bucle `for` y una variable `contador_mensaje` para personalizar el mensaje de entrada. Dependiendo del valor del contador, se asignan los valores a las variables **A**, **B**, **C**, y **D**.

```python
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
```

# Requisitos

Estos programas solo requieren tener Python 3 instalado.

# Ejemplo de Salida

```shell
Ingrese el valor de A: 5
Ingrese el valor de B: 3
Ingrese el valor de C: 8
Ingrese el valor de D: 1

Los valores ingresados fueron: A=5, B=3, C=8, D=1.
Los valores en orden ascendente son: [1, 3, 5, 8]
Los valores en orden descendente son: [8, 5, 3, 1]
```
