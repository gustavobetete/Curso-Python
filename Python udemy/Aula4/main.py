# For Loop - Utilizando Numeros

# imprimir de 1 a 5

for numero in range(6): # index de 0 1 2 3 4 5  ( ao total da 6 numeros )
    print(numero)

for numero in range(1, 6): # de 1 a 5 e não pega o numero 6
    print(numero)


for numero in range(1, 20, 2): # imprime apenas os numeros impares de 1 a 20 (step)
    print(numero)

# For Loop - Utilizando Strings

# imprimir Gustavo por letra
palavra = 'Fantastico'

for letra in 'Gustavo':
    print(letra)

for letra in palavra:
    print(f'{letra} esta dentro da palavra {palavra}')

# For Loop - Utilizando if e Else

# Enviar um email com os detalhes da compra online ( Maximo 3 tentativas) para compras confirmadas.

compra_confirmada = True
dados_compra = 'Compra no valor de R$12.50 e entrega confirmada'

for enviar in range(3):
    if compra_confirmada:
         print(dados_compra)
         print('Detalhes enviados para o seu email')
         break
else:
    print('Falha na compra')


# For Loop - Nested loops (Outer Loop e Inner Loop)

for numero1 in range(1,6):
    print('Produto' + str(numero1))
    for numero2 in range(11):
        print(numero1, numero2)

# For loop - Separando Strings

# Modificar de FANTASTICO para F A N T A S T I C O (horizontal)

palavra = 'FANTASTICO'

for spaco in palavra:
    print(spaco, end=' ')
   # print(f' {spaco}', end='') <<< pode ser assim tambem

# For Loop - Criando um retangulo
'''
Criar um retangulo de 6x6

@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
'''
linhas = 6
colunas = 6
simbolo = '@'

for l in range(linhas):
    for c in range(colunas):
        print(simbolo, end='')
    print()