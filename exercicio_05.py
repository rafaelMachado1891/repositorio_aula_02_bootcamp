# #### try-except e if

# 21: Conversor de Temperatura


print('exercicio_09- converta a temperatura de graus celsius para Fahrenheit')
try:    
    graus_celsius = float(input('digite a temperatura em graus celsius: '))
    Fahrenheit = graus_celsius * 9/5 + 32  
    resultado = Fahrenheit
    print('a temperatura da sua região em Fahrenheit é: ' , resultado,'\n')
except:
    ValueError
    print('digite uma valor valido')


# 22: Verificador de Palíndromo

try: 
    palavra = input('digite aqui uma palvra: ')
    texto_limpo = palavra.replace(' ','')
    texto_invertido = texto_limpo[::-1]
    resultado = texto_limpo == texto_invertido
    print(texto_invertido)
    print(resultado)
except: 
    ValueError('o texto inserido não é um palindromo')
# 23: Calculadora Simples
try: 

    primeiro_valor = input('insira um valor: ')
    soma = '+'
    subtracao = '-'
    multiplicacao = '*'
    divisao = '/'
    segundo_valor = input('insira um valor: ')
    resultado = primeiro_valor

except:
    ValueError


# 24: Classificador de Números
# 25: Conversão de Tipo com Validação