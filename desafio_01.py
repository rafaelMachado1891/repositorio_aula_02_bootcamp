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

salario = float(input("Digite o seu salário: "))



bonus_valor = float(input("Qual foi o valor do seu bonus? "))

bonus = 1000 + salario * bonus_valor

print("Seja bem vindo ",nome)

print("O valor total do seu bonus é: ", bonus)