while True:
    try:   
        termo_n = int(input("Qual o termo que você deseja saber na sequência de fibonacci? "))
        print()
        escolha = input("Você quer resolver fibonacci de maneira recursiva ou linear? ")
        if escolha.lower() != "recursiva" and escolha.lower() != "linear":
            print("Escolha inválida, digite recursiva ou linear!")
        print()

        if escolha.lower() == "recursiva":
            #De maneira recursiva:
            def fibonacci_recursivo(termo_n):
                if termo_n < 0:
                    return 
                elif termo_n == 0:
                    return 0
                
                elif termo_n == 1:
                    return 1
                
                else:
                    return fibonacci_recursivo(termo_n - 2) + fibonacci_recursivo(termo_n - 1)
                
            print(f'O valor correspondente de fib({termo_n}) utilizando a forma recursiva é: {fibonacci_recursivo(termo_n)}')
            break

        elif escolha.lower() == "linear":
            #De maneira linear
            def fibonacci_linear(termo_n):
                if termo_n < 0:
                    return
                elif termo_n == 0:
                    return 0
                elif termo_n == 1:
                    return 1

                anterior, atual = 0, 1
                for _ in range(2, termo_n + 1):
                    anterior, atual = atual, anterior + atual
                return atual
            
            print(f'O valor correspondente de fib({termo_n}) utilizando a forma linear é: {fibonacci_linear(termo_n)}')
            break

    except ValueError as e:
        print(e)