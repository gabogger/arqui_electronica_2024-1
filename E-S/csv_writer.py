from random import randint
import time

if __name__ == '__main__':
    inicio_cpu = time.perf_counter()
    codigo_base = 20240001
    contenido =  f"codigo,{','.join(f'lab{i+1}' for i in range(12))},e1,e2\n"

    for i in range(200):
        fila = f"{codigo_base + i},{','.join(str(randint(0,20)) for _ in range(14))}\n"
        contenido += fila

    contenido = contenido[:-1]

    fin_cpu = time.perf_counter()

    inicio_io = time.perf_counter()
    with open("notas.csv", "w+") as f:
        f.write(contenido)
    fin_io = time.perf_counter()

    print(f"tiempo de cpu: {fin_cpu - inicio_cpu} segundos \t\t tiempo de IO: {fin_io - inicio_io} segundos")

    
