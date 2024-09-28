num = int(input("insira um valor: "))


def sequenciaFibonacci(num):
    fibonacci = [0, 1]

    while True:
        valor = fibonacci[-1] + fibonacci[-2]

        if valor > num:
            break

        fibonacci.append(valor)    

    return fibonacci

def checkSequencia(numero):
    if numero < 0:
        return False
    
    fibonacci = sequenciaFibonacci(numero)

    if numero in fibonacci:
        return f"o número faz parte da sequência de fibonacci"
    else:
        return f"o número não faz parte da sequência de fibonacci"

resultado = checkSequencia(num) 
print(resultado)  