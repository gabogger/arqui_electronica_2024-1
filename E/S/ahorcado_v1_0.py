from typing import Union


palabra = "arquitectura"
intentos = 5
por_adivinar_list = ["_"] * len(palabra)


def encuentra_letra(word_list: list[str], letter: str, word_to_guess: str) -> Union[list[str], bool]: 
    letter_found = False
    word_to_guess_list = [*word_to_guess]
    for idx in range(len(word_list)):
        if letter == word_to_guess_list[idx]:
            letter_found = True
            word_list[idx] = letter
    
    return word_list, letter_found


if __name__ == '__main__':
    while True:
        letra = input(
            f"Palabra: {''.join(por_adivinar_list)}\t\tNumero de intentos restantes: {intentos}\n\nPor favor ingrese una letra: ")
        while len(letra) != 1:
            letra = input("Por favor ingrese una letra: ")
        
        por_adivinar_list, encontro = encuentra_letra(por_adivinar_list, letra, palabra)

        if not encontro:
            intentos -= 1

        if intentos == 0:
            print("Lo siento, perdio por maximo numero de intentos equivocados")
            exit(0)

        if not "_" in por_adivinar_list:
            print(f"Felicitaciones, encontro la palabra: {palabra}")
            exit(0)
        

