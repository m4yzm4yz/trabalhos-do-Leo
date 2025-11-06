import time
import random

def pesquisa_sequencial(lista, valor):
    comparacoes = 0
    for i, elemento in enumerate(lista):
        comparacoes += 1
        if elemento == valor:
            return i, comparacoes
    return -1, comparacoes

def pesquisa_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if lista[meio] == valor:
            return meio, comparacoes
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1, comparacoes


# Teste com lista de 100 números
lista = sorted(random.sample(range(1000), 100))
valor_procurado = random.choice(lista)

print("🔍 Teste de Busca")
print(f"Valor procurado: {valor_procurado}")

# Pesquisa Sequencial
inicio = time.time()
pos, comp_seq = pesquisa_sequencial(lista, valor_procurado)
tempo_seq = time.time() - inicio

# Pesquisa Binária
inicio = time.time()
pos, comp_bin = pesquisa_binaria(lista, valor_procurado)
tempo_bin = time.time() - inicio

print(f"Sequencial: {comp_seq} comparações | Tempo: {tempo_seq:.8f}s")
print(f"Binária:    {comp_bin} comparações | Tempo: {tempo_bin:.8f}s")
