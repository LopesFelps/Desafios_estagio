import json

def calcular_faturamento(arquivo_json):
    try:
        with open(arquivo_json) as file:
            dados = json.load(file)

        faturamento_diario = dados['faturamento_diario']
        
        # Filtra os dias com faturamento
        dias_faturamento = [valor for valor in faturamento_diario.values() if valor > 0]

        if not dias_faturamento:
            print("Não há faturamento registrado.")
            return

        menor_faturamento = min(dias_faturamento)
        maior_faturamento = max(dias_faturamento)
        media_faturamento = sum(dias_faturamento) / len(dias_faturamento)   
        
        # Conta os dias com faturamento acima da média
        dias_acima_media = sum(1 for valor in dias_faturamento if valor > media_faturamento)

        print(f"Menor faturamento: R${menor_faturamento:.2f}")
        print(f"Maior faturamento: R${maior_faturamento:.2f}")
        print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_json}' não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro: O arquivo JSON está mal formado.")

if __name__ == "__main__":
    calcular_faturamento('dados.json')