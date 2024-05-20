import time


if __name__ == '__main__':
    base_str = "*"
    res = list()

    for idx in range(1000):
        str_completo = base_str * (idx + 1)
        inicio = time.perf_counter()
        print(str_completo)
        fin = time.perf_counter()

        print(f"[{idx + 1}] Tiempo total de ejecucion: {fin - inicio} segundos")
        res.append(fin - inicio)

    promedio = sum(res) / len(res)
    maximo = max(res)
    minimo = min(res)

    print(f"Tiempo promedio de E/S {promedio}, maximo: {maximo}, minimo: {minimo}")