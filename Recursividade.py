def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def soma_lista(lista):
    if not lista:
        return 0
    return lista[0] + soma_lista(lista[1:])


# Testes com valores pequenos
print("\n🧮 Teste de Recursividade")
for i in range(1, 6):
    print(f"Fatorial({i}) = {fatorial(i)}")
for i in range(1, 10):
    print(f"Fibonacci({i}) = {fibonacci(i)}")

lista_teste = [1, 2, 3, 4, 5, 6, 7]
print(f"Soma recursiva da lista {lista_teste} = {soma_lista(lista_teste)}")
