# <<<<<<<<<<<<<<<<<<<Exercício 1>>>>>>>>>>>>>>>>>>>>
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
N = int(input("Quantas notas você deseja informar? "))
soma = 0

for i in range(N):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota
media = soma / N

print(f"A média aritmética das {N} notas é: {media:.2f}")

# <<<<<<<<<<<<<<<<<<<Exercício 3>>>>>>>>>>>>>>>>>>>>
numero = input("Digite um número: ")
numero_sem_sinal = numero.lstrip('-')
quantidade_digitos = len(numero_sem_sinal)
print(f"O número {numero} possui {quantidade_digitos} dígitos.")


# <<<<<<<<<<<<<<<<<<<Exercício 4>>>>>>>>>>>>>>>>>>>>
soma = 0

while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    
    if numero == 0:
        break  # Encerra o loop se o número for 0
    
    soma += numero  # Adiciona o número à soma

print(f"A soma dos números digitados é: {soma}")
