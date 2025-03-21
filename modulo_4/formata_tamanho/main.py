import math


def formata_tamanho(tamanho: int, base: int = 1024) -> str:

    if tamanho <= 0:
        return "0B"

    abreviacao_tamanhos = 'B', 'KB', 'MB', 'GB', 'TB'

    indice_abreviacao_tamanhos = int(math.log(tamanho, base))

    potencia = base ** indice_abreviacao_tamanhos

    tamanho_final = tamanho / potencia

    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


print(formata_tamanho(1000))
print(formata_tamanho(1000000))
print(formata_tamanho(100000000))
