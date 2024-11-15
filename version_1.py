
# Ingreso de valores y creación de la lista
valores = [int(input(f"Ingrese el valor de {var}: ")) for var in ["A", "B", "C", "D"]]

# Ordenar la lista en orden ascendente y descendente
lista_orden = sorted(valores)
lista_orden_inverso = sorted(valores, reverse=True)

# Mostrar la información
print(f"Los valores ingresados fueron: A={valores[0]}, B={valores[1]}, C={valores[2]}, D={valores[3]}.")
print(f"Los valores en orden ascendente son: {lista_orden}")
print(f"Los valores en orden descendente son: {lista_orden_inverso}")
