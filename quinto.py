def inverter_string(s):
    string_invertida = ""
    # Percorre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

if __name__ == "__main__":
    # String pode ser definida aqui ou informada pelo usuário
    string_original = input("Informe uma string para inverter: ")
    
    resultado = inverter_string(string_original)
    print(f"String invertida: {resultado}")