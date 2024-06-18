# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

print('exercicio_06- efetue a soma dos valores')
primeiro_valor = float(input('digite o primeiro valor: '))
segundo_valor = float(input('digite o segundo valor: '))
resultado = primeiro_valor + segundo_valor
print(resultado,'\n')


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
print('exercicio_07- calcule a media dos valores')
primeiro_valor = float(input('digite o primeiro valor: '))
segundo_valor = float(input('digite o segundo valor: '))
resultado = primeiro_valor + segundo_valor
media = resultado / 2 
print(media,'\n')

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
print('exercicio_08- calcule a potencia de um numero')
primeiro_valor = float(input('digite o valor da base: '))
segundo_valor = float(input('digite o valor da potencia: '))
resultado = primeiro_valor ** segundo_valor

print(resultado,'\n')


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

print('exercicio_09- converta a temperatura de graus celsius para Fahrenheit')
graus_celsius = float(input('digite a temperatura em graus celsius: '))
Fahrenheit = graus_celsius * 9/5 + 32  
resultado = Fahrenheit

print('a temperatura da sua região em Fahrenheit é: ' , resultado,'\n')

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
print('exercicio_10- calcule a area de um circulo apartir do raio')
valor_raio = float(input('digite o valor do raio: '))
pi= 3.14156
resultado = valor_raio ** 2 * pi

print(resultado,'\n')


#raio_do_circulo = float(input("Digite o raio: "))
#area_do_circulo = math.pi * raio_do_circulo ** 2
# area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
#print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_de_dia_mes_ano = data_do_usuario.split("/")
# print(f"O elemento 1 e o: {lista_de_dia_mes_ano[0]}")
# print(f"O elemento 2 e o: {lista_de_dia_mes_ano[1]}")
# print(f"O elemento 3 e o: {lista_de_dia_mes_ano[2]}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação