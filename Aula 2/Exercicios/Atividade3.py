# <<<<<<<<<<<<<<<<<<<Exercício 1>>>>>>>>>>>>>>>>>>>>
nota = float(input("Digite a nota do aluno: "))
if nota < 7:
    print("Aluno reprovado.")
else:
    print("Aluno aprovado.")

# <<<<<<<<<<<<<<<<<<<Exercício 2>>>>>>>>>>>>>>>>>>>>
idade = int(input("Digite a idade do nadador: "))
if 5 <= idade <= 7:
    print("Categoria: Infantil 1")
elif 8 <= idade <= 11:
    print("Categoria: Infantil 2")
elif 12 <= idade <= 13:
    print("Categoria: Juvenil 1")
elif 14 <= idade <= 17:
    print("Categoria: Juvenil 2")
elif idade >= 18:
    print("Categoria: Adulto")
else:
    print("Idade fora das categorias disponíveis.")
