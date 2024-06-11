'''
desenhe e implemente uma pequena aplicação em Python, chamada
Meu Compressor Básico (MCB).
O MCB deve funcionar da seguinte forma:

1. Uma lista de palavras únicas deve ser criada a partir de uma string digitada.
Por exemplo, dada a string:
“A iva e a zita e a ana dizem ola ana ola iva ola”

2. A string base deve ser completamente destruída.

3. Finalmente, a partir da lista de palavras únicas deve reconstruir a string original
(que foi completamente destruída, não podendo haver uma cópia dela em parte
nenhuma).

4. Naturalmente, no seu algoritmo que vai desenvolver, o programa deve guardar
as posições de cada palavra repetida de forma a poder reinseri-las nos locais
apropriados.
'''
def criar_lista(frase):
    palavras = frase.split()
    lista_unica = []
    posicoes = {}

    for i, palavra in enumerate(palavras):
        if palavra not in lista_unica:
            lista_unica.append(palavra)
            posicoes[palavra] = [i]
        else:
            posicoes[palavra].append(i)
    
    return lista_unica, posicoes

def reconstruir_frase(lista_unica, posicoes):
    total_palavras = sum(len(indices) for indices in posicoes.values())
    frase_reconstruida = [""] * total_palavras

    for palavra, indices in posicoes.items():
        for i in indices:
            frase_reconstruida[i] = palavra
    
    return " ".join(frase_reconstruida)

def main():
    frase = input("Digite uma frase: ")
    
    # Criar lista de palavras únicas e guardar posições
    lista_unica, posicoes = criar_lista(frase)
    
    # Destruir a string base (removendo a referência)
    del frase
    
    # Reconstruir a string original
    frase_reconstruida = reconstruir_frase(lista_unica, posicoes)
    
    print("\nLista de palavras únicas:")
    for palavra in lista_unica:
        print(palavra)
    
    print("\nPosições das palavras:")
    for palavra, indices in posicoes.items():
        print(f"{palavra}: {indices}")
    
    print("\nString reconstruída:")
    print(frase_reconstruida)

if __name__ == "__main__":
    main()

