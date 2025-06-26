quantidade = 0
total_alunos = 0
turma_atual = 0
entrada = ""
eh_numero = 0
indice = 0
num_aluno = 0

while quantidade <= 0:
    entrada = input("Quantidade de turmas: ")
    eh_numero = 1
    indice = 0

    while indice < 100 and entrada[indice:indice+1]:
        if entrada[indice] not in "0123456789":
            eh_numero = 0