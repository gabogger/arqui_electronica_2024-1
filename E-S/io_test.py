import time


if __name__ == '__main__':
    inicio = time.perf_counter()
    print("Este es un print para evaluar")
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {fin - inicio} segundos")
    