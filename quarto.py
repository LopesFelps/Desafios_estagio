def calcular_percentuais(faturamento):
    total = sum(faturamento.values())
    
    print("Faturamento por estado:")
    for estado, valor in faturamento.items():
        percentual = (valor / total) * 100
        print(f"{estado}: R${valor:.2f} - {percentual:.2f}%")

if __name__ == "__main__":
    faturamento_mensal = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }

    calcular_percentuais(faturamento_mensal)