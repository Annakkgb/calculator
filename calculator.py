def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero!"

# Função para exibir o menu :)
def exibir_menu():
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")

# Loop :)
while True:
    exibir_menu()
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 0:
        print("Calculadora encerrada.")
        break

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = soma(numero1, numero2)
        print("Resultado: ", resultado)
    elif opcao == 2:
        resultado = subtracao(numero1, numero2)
        print("Resultado: ", resultado)
    elif opcao == 3:
        resultado = multiplicacao(numero1, numero2)
        print("Resultado: ", resultado)
    elif opcao == 4:
        resultado = divisao(numero1, numero2)
        print("Resultado: ", resultado)
    else:
        print("Opção inválida. Por favor, tente novamente.")