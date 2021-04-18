# CHECKPOINT 2 CPT

#quantidade de Pratos Principais
pratosPrincipais = int(input("Quantos pratos principais: "))
while (pratosPrincipais <= 0):
    print("Número de pratos principais inválido. Digite novamente.")
    pratosPrincipais = int(input("Quantos pratos principais: "))

if (pratosPrincipais > 3):
    descontoPratos = 0.04
else:
    descontoPratos = 0

#Valor total da nota
valorTotalNota = float(input("Valor total da nota: R$"))
while (valorTotalNota <= 0):
    print("Valor inválido. Digite novamente.")
    valorTotalNota = float(input("Valor total da nota: R$"))
    
if (valorTotalNota > 500):
    descontoTotalNota = 0.06
else:
    descontoTotalNota = 0
    
#Cupom de desconto
temCupom = input("Tem cupom[S/N]: ").upper()
while (temCupom != "S" and temCupom != "N"):
    print("Cupom inválido..., Digite 'S' ou 'N'...")
    temCupom = input("Tem cupom[S/N]: ").upper()


if (temCupom == "S"):
    codCupom = input("Digite o código do cupom: ").upper()
    while (codCupom != "BORALA10" and codCupom != "BORALA05"):
        print("Cupom inválido...")
        continuar = input("Deseja tentar outro código?[S/N]: ").upper()
        while (continuar != "S" and continuar != "N"):
            print("Inválido... Digite 'S' ou 'N'...")
            continuar = input("Deseja tentar outro código?[S/N]: ").upper()
        if (continuar == "S"):
            codCupom = input("Digite o código do cupom: ").upper()
        else:
            cupom = 0
            break
    if (codCupom == "BORALA10"):
        cupom = 0.1
    elif (codCupom == "BORALA05"):
        cupom = 0.05
else:
    print("Sem cupom.")
    cupom = 0


primeiraVez = input("É a primeira vez no restaurante[S/N]? ").upper()
while (primeiraVez !="S" and primeiraVez != "N"):
    print("Valor inválido. Digite novamente.")
    primeiraVez = input("É a primeira vez no restaurante[S/N]? ").upper()

if (primeiraVez == "S"):
    descontoPrimeiraVez = 0.05
else:
    descontoPrimeiraVez = 0


descontosTotal = descontoPratos + descontoPrimeiraVez + descontoTotalNota + cupom

if (descontosTotal == 0):
    valorFinal = valorTotalNota
else:
    valorFinal = valorTotalNota - ( valorTotalNota * descontosTotal ) 



racharConta = input("Deseja rachar a conta[S/N]: ").upper()
while (racharConta != "S" and racharConta != "N"):
    print("Inválido... Digite 'S' ou 'N'...")
    racharConta = input("Deseja rachar a conta[S/N]? ")

if (racharConta == "S"):
    qtdPessoas = int(input("Deseja dividir a conta em quantas pessoas: "))
    valorRachado = valorFinal / qtdPessoas
    print('-' * 50)
    if (descontosTotal <= 0):
        print(f"Valor total da nota fiscal: R${valorTotalNota:.2f}")
        print(f"Não tiveram descontos.")
        print(f"\nNúmero de pessoas: {qtdPessoas}")
        print(f"Total por pessoa: R${valorRachado:.2f}")
    else:
        print(f"Valor total da nota fiscal: R${valorTotalNota:.2f}")
        print(f"Valor total da nota com desconto: R${valorFinal:.2f}")
        print(f"\nNúmero de pessoas: {qtdPessoas}")
        print(f"Total por pessoa: R${valorRachado:.2f}")
    print('-' * 50)
    
else:
    print('-' * 50)
    if (descontosTotal <= 0):
        print(f"Valor total da nota fiscal: R${valorTotalNota:.2f}")
    else:
        print(f"Valor total da nota fiscal: R${valorTotalNota:.2f}")
        print(f"Valor total da nota com desconto: R${valorFinal:.2f}")
    print('-' * 50)