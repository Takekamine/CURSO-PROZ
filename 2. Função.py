def calculadora():
    num1=float(input("Digite o primeiro número: "))
    num2=float(input("Digite o segundo número: "))
    conta=int(input("Digite a operação desejada:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n"))
    if conta==1:
        resultado=num1+num2
    elif conta==2:
        resultado=num1-num2
    elif conta==3:
        resultado=num1*num2
    elif conta==4:
        resultado=num1/num2
    print("Resultado:", resultado)

calculadora()
