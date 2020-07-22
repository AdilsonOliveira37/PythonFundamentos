#Calculadora em Python

soma = lambda x,y: x+y
subtracao = lambda x,y: x-y
multiplicacao = lambda x,y: x*y
divisao = lambda x,y: x/y

print("*************** Python Calculator *****************")

print("\n Selecione o número da operação desejada:\n")

print("1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão")

operacao = int(input("\nDigite a sua opção [ 1 | 2 | 3 | 4 ]:\n"))
num1 = float(input("Insira o primeiro número:"))
num2 = float(input("Insira o segundo número:"))

if (operacao == 1): 
    print(soma(num1,num2))
    
elif(operacao == 2):
    print(subtracao(num1,num2))

elif(operacao == 3 ):
    print(multiplicacao(num1,num2))

elif(operacao == 4):
    if(num2 != 0):
        print(divisao(num1,num2))
    print("Divisão por 0")

else: 
    print("Operação inválida!")