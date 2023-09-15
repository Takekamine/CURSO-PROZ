def soma(num1,num2):
    resultado=num1+num2
    return resultado

def subtracao(num1,num2):
    ordem=int(input(f"Escolha a opção de conta:\n1 - {num1} - {num2}\n2 - {num2} - {num1}\n"))
    if ordem==1:
        resultado=num1-num2
    elif ordem==2:
        resultado=num2-num1
    else:
        print('Errou')
    return resultado

def multiplicacao(num1,num2):
    resultado=num1*num2
    return resultado

def divisao(num1,num2):
    ordem=int(input(f"Escolha a opção de conta:\n1 - {num1} / {num2}\n2 - {num2} / {num1}\n"))
    if ordem==1:
        resultado=num1/num2
    elif ordem==2:
        resultado=num2/num1
    else:
        print('Errou')
    return resultado

def main():
    while True:
        opcao=int(input("Escolha a operação desejada:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n0 - Sair\n"))
        if opcao==1:
            print("\nAdição")
            num1=float(input("Digite o 1º número: "))
            num2=float(input("Digite o 2º número: "))
            print(f"Resultado: {soma(num1,num2)}\n")

        elif opcao==2:
            print("\nSubtração")
            num1=float(input("Digite o 1º número: "))
            num2=float(input("Digite o 2º número: "))
            print(f"Resultado: {subtracao(num1,num2)}\n")

        elif opcao==3:
            print("Multiplicação")
            num1=float(input("Digite o 1º número: "))
            num2=float(input("Digite o 2º número: "))
            print(f"Resultado: {multiplicacao(num1,num2)}\n")

        elif opcao==4:
            print("Divisão")
            num1=float(input("Digite o 1º número: "))
            num2=float(input("Digite o 2º número: "))
            print(f"Resultado: {divisao(num1,num2)}\n")

        elif opcao==0:
            break

        else:
            print("Essa opção não existe.")        

            
main()
