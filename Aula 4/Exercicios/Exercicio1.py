# <<<<<<<<<<<<<<<<<<<Exercício 1>>>>>>>>>>>>>>>>>>>>

# nota = int(input("Digite uma nota entre 0 e 10: "))

# if nota >= "0" and <= "10":
#     print(f"Você digitou a nota {nota}")
# erro = print("Erro: nota inválida!")
# else:
#     erro = print("Erro: nota inválida!")

# --Versão do chat
while True:
    try:
        nota = int(input("Digite uma nota entre 0 e 10: "))
        if 0 <= nota <= 10:
            print(f"Você digitou a nota {nota}")
            break
        else:
            print("Erro: nota inválida! Tente novamente.")
    except ValueError:
        print("Erro: você deve digitar um número inteiro.")

# <<<<<<<<<<<<<<<<<<<Exercício 2>>>>>>>>>>>>>>>>>>>>
