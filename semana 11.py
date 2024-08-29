# Diccionario inicial con palabras en inglés y español
diccionario_esp_ing = {
    "tiempo": "time",
    "persona": "person",
    "año": "year",
    "camino": "way",
    "forma": "way",
    "día": "day",
    "cosa": "thing",
    "hombre": "man",
    "mundo": "world",
    "vida": "life",
    "mano": "hand",
    "parte": "part",
    "niño": "child",
    "niña": "child",
    "ojo": "eye",
    "mujer": "woman",
    "lugar": "place",
    "trabajo": "work",
    "semana": "week",
    "caso": "case",
    "punto": "point",
    "tema": "point",
    "gobierno": "government",
    "empresa": "company",
    "compañía": "company"
}

# Diccionario inverso para traducción de inglés a español
diccionario_ing_esp = {v: k for k, v in diccionario_esp_ing.items()}


# Función para traducir una frase
def traducir_frase(frase, idioma):
    palabras = frase.lower().split()
    traduccion = []

    if idioma == "español":
        for palabra in palabras:
            if palabra in diccionario_esp_ing:
                traduccion.append(diccionario_esp_ing[palabra])
            else:
                traduccion.append(palabra)
    elif idioma == "inglés":
        for palabra in palabras:
            if palabra in diccionario_ing_esp:
                traduccion.append(diccionario_ing_esp[palabra])
            else:
                traduccion.append(palabra)

    return " ".join(traduccion)


# Función para agregar palabras al diccionario
def agregar_palabra():
    palabra_espanol = input("Ingrese la palabra en español: ").lower()
    palabra_ingles = input("Ingrese la palabra en inglés: ").lower()

    if palabra_espanol not in diccionario_esp_ing and palabra_ingles not in diccionario_ing_esp:
        diccionario_esp_ing[palabra_espanol] = palabra_ingles
        diccionario_ing_esp[palabra_ingles] = palabra_espanol
        print(f"Palabra '{palabra_espanol}' y su traducción '{palabra_ingles}' agregadas con éxito.")
    else:
        print("La palabra ya existe en el diccionario.")


# Función principal del menú
def menu():
    while True:
        print("\nMENU\n" + "="*55)
        print("1. Traducir una frase")
        print("2. Ingresar más palabras al diccionario")
        print("0. Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            idioma = input("Ingrese el idioma de origen ('español' o 'inglés'): ").lower()
            if idioma not in ["español", "inglés"]:
                print("Idioma no válido. Intente nuevamente.")
                continue
            frase = input("Ingrese la frase: ")
            print("Su frase traducida es:", traducir_frase(frase, idioma))
        elif opcion == "2":
            agregar_palabra()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


# Ejecutar el programa
menu()
