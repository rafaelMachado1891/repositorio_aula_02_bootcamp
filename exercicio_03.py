# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
conversao = input('Insira seu texto aqui: ')
resultado = conversao.upper()
print(resultado, '\n')


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input('insira seu nome: ')
resultado = nome.upper()
print(resultado,'\n')

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input('insira aqui seu texto: ')
resultado = frase.strip()
print(resultado,'\n')

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
date = input('insira uma data no formato dd/mm/yyyy: ')
resultado = date.split('/')
print('o dia da data é: ', resultado[0])
print('o mes da data é: ', resultado[1])
print('o ano da data é: ', resultado[2], '\n')


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
texto = input('insira aqui seu texto: ')
texto_2 = input('insira a segunda opção de texto: ')
resultado = texto + texto_2
print(resultado,'\n')