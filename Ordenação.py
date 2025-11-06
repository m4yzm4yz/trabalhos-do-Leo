import time
import random

def ordenacao_selecao(lista):
    n = len(lista)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    return quicksort(menores) + iguais + quicksort(maiores)


# Teste com 1000 elementos
lista_original = [random.randint(0, 10000) for _ in range(1000)]

print("\n🔄 Teste de Ordenação")

# Seleção
inicio = time.time()
ordenacao_selecao(lista_original[:])
tempo_selecao = time.time() - inicio

# Quicksort
inicio = time.time()
quicksort(lista_original[:])
tempo_quick = time.time() - inicio

# Sorted()
inicio = time.time()
sorted(lista_original)
tempo_sorted = time.time() - inicio

print(f"Seleção: {tempo_selecao:.5f}s")
print(f"Quicksort: {tempo_quick:.5f}s")
print(f"Sorted(): {tempo_sorted:.5f}s")
