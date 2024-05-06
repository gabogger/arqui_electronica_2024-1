from random import randint
from typing import Union

# palabras = ["arquitectura", "computadoras", "universidad", "alumnos", "profesores", "campus"]
# palabra = palabras[randint(0, len(palabras) - 1)]
intentos = 5
por_adivinar_list = list()

letras_incorrectas = list()
letras_correctas = list()

def carga_lista() -> list[str]:
    with open("palabras.arqui", "r") as f:
        contenido = f.read()
    palabras = contenido.split("\n")

    return palabras

def selecciona_palabra(lista_palabras: list[str]) -> str:
    global por_adivinar_list
    palabra = lista_palabras[randint(0, len(lista_palabras) - 1)]
    por_adivinar_list = ["_"] * len(palabra)

    return palabra


def encuentra_letra(word_list: list[str], letter: str, word_to_guess: str) -> Union[list[str], bool]: 
    letter_found = False
    for idx in range(len(word_list)):
        if letter == word_to_guess[idx]:
            letter_found = True
            word_list[idx] = letter
    
    return word_list, letter_found


if __name__ == '__main__':
    print("Bienvenidos al juego de ahorcado, cargando configuracion...")
    palabras = carga_lista()
    palabra = selecciona_palabra(palabras)
    while True:
        letra = input(
            f"Palabra: {''.join(por_adivinar_list)}\nNumero de intentos restantes: {intentos}\t\tLetras incorrectas: {', '.join(letras_incorrectas)}\n\nPor favor ingrese una letra: ")

        while len(letra) != 1:
            if letra.lower() == "salir":
                print("Saliendo del juego")
                exit(1)

            letra = input("Por favor ingrese una letra: ")
        
        if letra in letras_incorrectas or letra in letras_correctas:
            print("Letra ya fue ingresada previamente")
            continue

        por_adivinar_list, encontro = encuentra_letra(por_adivinar_list, letra, palabra)

        if not encontro:
            letras_incorrectas.append(letra)
            intentos -= 1
        else:
            letras_correctas.append(letra)

        if intentos == 0:
            print("Lo siento, perdio por maximo numero de intentos equivocados")
            exit(0)

        if not "_" in por_adivinar_list:
            print(f"Felicitaciones, encontro la palabra: {palabra}")
            exit(0)
        

