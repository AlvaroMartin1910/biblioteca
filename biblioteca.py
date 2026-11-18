"""Programa que nos deja prestar libros durante un numero de dias que el usuario elija"""

def prestar(libro, dias):
    """Funcion que hace que pueda prestarnos el libro

    :param libro: nombre del libro que se vaya a elegir.
    :param dias: numero de dias que el libro va a ser prestado.
    :return: nombre del libro y cuantos dias va a ser prestado.
    """
    return f"{libro} prestado {dias} días"

if __name__ == "__main__":
    print(prestar("El Quijote", 15))