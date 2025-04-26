def busqueda_binaria(lista_numeros: list[int], numero) -> int:
	minimo = 0
	maximo = len(lista_numeros) - 1
	mitad = (minimo + maximo) // 2

	while minimo < maximo:

		if numero > lista_numeros[mitad]:
			minimo = mitad + 1
		elif numero < lista_numeros[mitad]:
			maximo = mitad - 1
		else:
			return mitad

		mitad = (minimo + maximo) // 2

	return -1
			

print(busqueda_binaria([11, 25, 3, -4, 95], 9))


# ---------- Ejercicio b ----------
def max_min(lista_elementos: list[any]) -> None:
	minimo = maximo = lista_elementos[0]

	for i in lista_elementos:
		if maximo < i:
			maximo = i
		elif minimo > i:
			minimo = i

	print(f"El valor máximo es {maximo}")
	print(f"El valor mínimo es {minimo}")

	return None


max_min([11,25, 3, -4, 95])


# ---------- Ejercicio c ----------
def lista_aumentada(lista_numeros: list[int]) -> list[int]:
	lista_resultado = list()

	for x in lista_numeros:
		lista_resultado.append(x + 1)

	return lista_resultado

print(lista_aumentada([0 ,1 ,2 ,3 ,4]))


# ---------- Ejercicio d ----------
def lista_palabras_a(lista_palabras: list[str]) -> list[str]:
	lista_resultado = list()

	for palabra in lista_palabras:
		if palabra[0] == 'a' or palabra[0] == 'A':
			lista_resultado.append(palabra)

	return lista_resultado


print((lista_palabras_a([ "arbol" , "barco" , "artificial" , "casa" , "dado" , "a" ])))


# ---------- Ejercicio e ----------
def lista_inversa(lista_elementos: list[any]) -> list[any]:

	lista_resultado = list()
	ultima_pos = len(lista_elementos) - 1

	while ultima_pos >= 0:
		lista_resultado.append(lista_elementos[ultima_pos])
		ultima_pos -= 1

	return lista_resultado

print(lista_inversa([0 ,1 ,2 ,3 ,4 ,5]))
	
