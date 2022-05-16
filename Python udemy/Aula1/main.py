# programa de uma calculadora simples

# Somar
def soma(x, y):
    return x + y

# Subtrair
def subtrair(x, y):
    return x - y

# Multiplicar
def multiplicar(x, y):
    return x * y

#Dividir

def divide(x, y):
    return x / y

print("Seleciona a operação.")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

while True:
    # pega resposta do usuario
    choice = input("Selecione a operação(1/2/3/4): ")

    #Checa qual numero foi selecionado
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Entre com o primeiro numero: "))
        num2 = float(input("Entre com a segundo numero: "))

        if choice == '1':
            print(num1, "+", num2, "=", soma(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtrair(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiplicar(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Numero invalido")