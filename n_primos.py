n = int(input("Até qual número você quer saber os primos? "))
escolha = input("Você quer calcular de forma linear ou recursiva? ")

def eh_primo(numero, divisor=None):
    if divisor is None:
        divisor = int(numero**0.5)

    if numero <= 1:
        return False
        
    if divisor < 2:
        return True
            
    if numero % divisor == 0:
        return False
        
    return eh_primo(numero, divisor -1)

if escolha.lower() == "recursiva":
    #De forma recursiva
    def listar_primos_recursivos(n):
        if n < 2:
            return []
        
        if eh_primo(n):
            return listar_primos_recursivos(n-1) + [n]
        
        else:
            return listar_primos_recursivos(n-1)
        
    print(f"Números primos até {n} usando recursividade: {listar_primos_recursivos(n)}")

if escolha.lower() == "linear":
    #De forma linear
    def eh_primo_linear(n):
            primos = []
            for i in range(2, n+1):
                if eh_primo(i):
                    primos.append(i)

            return primos
        
    print(f"Números primos até {n} de forma linear: {eh_primo_linear(n)}")