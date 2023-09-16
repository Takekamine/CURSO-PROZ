nome=input("Digite seu nome: ")
idadee=int(input("Digite o ano de nascimento: "))
idade=2023-idadee

if idadee>=1922 and idadee<=2022:
    print(f"Seu nome é: {nome} e irá completar {idade} anos em 2023!")
else:
    print("Seu ano de nascimento ta errado, suponho que não tenha mais de 100 anos nem menos de 1")       
