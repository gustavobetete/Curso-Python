# == While Loops ==

# Excelente para loops dependentes de uma condição.

# Criar uma promoção para um produto no valor de R$100.

valor = 100
dia = 0

while valor > 20:
    dia += 1
    print(f'No dia {dia} o produto vai ser vendido por R${valor}')
    valor -= 5

# Criando condições com While Loop

# Publicar um produto com comissão de 10% se for acima de R$20.

valor2 = int(input('Digite o valor do seu Produto em R$: '))

while valor2 > 20:
    valor2 = (valor2 * 0.10) + valor2
    print(f'O valor final do seu produto será de R${valor2}')
    break