def filtrar_pares(tuplo):
    pares = tuple(x for x in tuplo if x % 2 == 0)
    return pares

tuplo_str = input("Insira um tuplo de inteiros positivos: ")
tuplo = tuple(map(int, tuplo_str.split(',')))
pares = filtrar_pares(tuplo)
print("Algarismos pares:", pares)
