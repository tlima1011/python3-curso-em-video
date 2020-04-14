def verificarPalindromo(frase):
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''
    palindromo = ''
    for letra in range(len(junto) -1, -1, -1):
        inverso += junto[letra]
    print('O inverso de {} é {}' .format(junto, inverso))
    if junto == inverso:
        palindromo = 'Temos um palíndromo!!!'
    else:
        palindromo = 'Não temos um palindromo!!!'
    return palindromo