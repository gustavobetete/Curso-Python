# Logical Operators (Operadores Logicos)

# Utilizando if else

velocidade = 105

if velocidade > 110:
    print("Voce esta muito rapido, favor reduzir")
elif velocidade < 60:
    print("Favor dirigir acima de 80Km/h")
else:
    print("Velocidade ok")

# outro exemplo de if else (com boolean)

renda_acima_5mil = True
nome_limpo = False

if renda_acima_5mil and nome_limpo:
    print("Financiamento aprovado")
else:
    print("Financiamneto negado")

renda_acima_5mil = True
nome_limpo = False

if renda_acima_5mil or nome_limpo:
    print("Financiamento aprovado")
else:
    print("Financiamneto negado")

# Ternary Operator (Operador Ternário)

idade = 12

if idade < 16:
    print("Voce não pode votar ainda, a idade minima é 16 anos")
else:
    print("Voce pode votar!")

# agora tudo em uma linha
resultado = 'Voto Permitido' if idade >= 16 else 'Voto não permitido'
print(resultado)

# Multiple Comparison Operators ( Multiplos Operadores de comparação)

valor = 20

#if valor >= 20 and valor < 40: <<<< esse é a mesma coisa do de baixo
if 20 <= valor < 40:
    print('Produto foi Aceito')
else:
    print('Produto não aceito')