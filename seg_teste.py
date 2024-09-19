def fibonacci_sequence(n):
    fib_seq = [0, 1]
    while True:
        next_fib = fib_seq[-1] + fib_seq[-2]
        if next_fib > n:
            break
        fib_seq.append(next_fib)
    return fib_seq

def main():
    # Número pode ser definido aqui
    numero_informado = int(input("Informe um número: "))

    # Gera a sequência de Fibonacci até o número informado
    fib_seq = fibonacci_sequence(numero_informado)

    # Verifica se o número informado está na sequência
    if numero_informado in fib_seq:
        print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()