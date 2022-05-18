# utilizando slice (fatiar)

fruta = 'Abacate'
#index   0123456

print(fruta[2:6])# do index 2 ate o 6 - lembrando que sempre no final pega 1 antes ( então vai aparecer do 2:5)

valor = 99.75
#index  01234
valor = str(valor)

print(valor[3:4])# do index 3 ate o 4 - lembrando que sempre no final pega 1 antes ( então vai aparecer do 3:3)
print(valor[:4]) # de todo o index ate o 4
print(valor[2:]) # do index 2 ate o final

# formatar string

# jeito casual
nome = 'Gustavo'
sobrenome = 'Betete'
profissao = 'Programador'

texto = 'O ' + nome + ' ' + sobrenome + ' é um ' + '[' + profissao + ']'
print(texto)

# jeito formatado

texto2 = f'O {nome} {sobrenome} é um excelente [{profissao}]'
print(texto2)

'''
# utilizar input

idade = input("Qual é a sua idade?")
print(idade + ' anos')
'''

# utilizando LowerCase e UpperCase

mensagem = 'eu adoro comida Caseira'

print(mensagem.lower())# coloca toda mensagem em minusculo
print(mensagem.upper())# coloca toda mensagem em maiusculo
print(mensagem.capitalize()) # coloca a primeira letra em maiusculo
print(mensagem.find('c')) # procura se tem a letra desejavel (index)
print(mensagem.replace('a', 'e'))# o que eu quero encontrar e trocar pelo oq
print(mensagem.replace('Caseira', 'feita em casa'))
print(mensagem.strip())# remove qualquer espaço antes do primeiro caracter
