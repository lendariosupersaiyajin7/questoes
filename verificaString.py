texto = input("insira uma frase: ")

def encontrarLetra(text):
    contador = 0

    for a in texto:
        
        if a.lower() == 'a' or a.upper() == 'A':
            contador += 1
        else:
            contador += 0
    return f"a quantidade de vezes que a letra A aparece é: {contador}"

result = encontrarLetra(texto)
print(result)

