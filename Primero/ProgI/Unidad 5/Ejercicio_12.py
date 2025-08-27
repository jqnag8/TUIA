def contar_apariciones(texto: str) -> dict():
    lista_palabras = texto.split(sep = " ")
    diccionario_contador_palabras = dict()

    for palabra in lista_palabras:
        if palabra in diccionario_contador_palabras:
            diccionario_contador_palabras[palabra] += 1
        else:
            diccionario_contador_palabras[palabra] = 1

    return diccionario_contador_palabras


print(contar_apariciones("Hola, hoy es un día muy especial."))
