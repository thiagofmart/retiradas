def calcular_retirada(tempo, capital):
    return capital * 0.01


def calcular_variacao(tempo, capital, retiradas):
    return (capital * tempo * 4) - sum(retiradas)


def calcular_retiradas_continua(meses, capital_inicial):
    retiradas = []
    capital_acumulado = capital_inicial
    for t in range(1, meses + 1):
        capital_acumulado = calcular_variacao(t, capital_inicial, retiradas)
        retirada = calcular_retirada(t, capital_acumulado)
        retiradas.append(retirada)
        print(f"retirada:{retirada}\ncapital_acumulado: {capital_acumulado}\n")
    return retiradas


retiradas = calcular_retiradas_continua(12, 60_000)
sum(retiradas)
