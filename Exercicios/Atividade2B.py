num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação matemática a ser realizada (+, -, x, /, **, %): ")

if operacao == "+":
    soma = num1+num2
    print(f"A soma de {num1} + {num2} é {soma}")

elif operacao == "-":
    subtracao = num1-num2
    print(f"A subtração de {num1} - {num2} é {subtracao}")

elif operacao == "x":
    multipicacao = num1*num2
    print(f"A multiplicação de {num1} x {num2} é {multipicacao}")

elif operacao == "/":
    if num2 != 0:
        divisao = num1/num2
        print(f"A divisão de {num1} e {num2} é {divisao}")
    else:
        print("Erro: divisão por zero!")

elif operacao == "**":
    exponencial = num1**num2
    print(f"A exponenciação de {num1} e {num2} é {exponencial}")

elif operacao == "%":
    if num2 != 0:
        modulo = num1 % num2
        print(f"O módulo de {num1} % {num2} é {modulo}")
    else:
        print("Erro: módulo por zero!")
else: 
    print("Operação inválida!")