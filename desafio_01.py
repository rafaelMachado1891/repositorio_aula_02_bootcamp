nome = input("Digite o seu nome: ")

if  nome.isdigit():
    print('você digitou um valor invalido: ')
    exit()
elif len(nome) == 0:
    print('você não digitou nada: ')
    exit()
elif nome.isspace():
    print('você digitou somente espaco')
    exit()

try:
    salario = float(input("Digite o seu salário: "))
    if salario < 0:
        print('insira uma valor valido para o salário')
except: 
    ValueError
    print('Você inseriu o seu salario errado, digite um valor valido')
    exit()

try: 
    bonus_valor = float(input("Qual foi o valor do seu bonus? "))

    if bonus_valor < 0:
     print('Insira um valor positivo para o bonus')

except:
    ValueError
    print('insira um valor decimal para o bônus')
    NameError
    print('você inseriu um valor invalido para o bonus, digite uma valor no formato decimal separado por "." ')
    exit()

bonus = 1000 + salario * bonus_valor
 

print("O valor total do seu bonus é: ", bonus)