lista = [10, 20, 30]
print("Lista inicial:", lista)

lista.append(40)
print("Após append(40):", lista)  # [10, 20, 30, 40]

lista.insert(1, 15)
print("Após insert(1, 15):", lista)  # [10, 15, 20, 30, 40]

lista.remove(20)
print("Após remove(20):", lista)  # [10, 15, 30, 40]

lista.sort()
print("Após sort():", lista)  # [10, 15, 30, 40]

lista.reverse()
print("Após reverse():", lista)  # [40, 30, 15, 10]

print("Quantidade de vezes que 10 aparece:", lista.count(10))  # 1

ultimo = lista.pop()
print("Elemento removido com pop():", ultimo)  # 10
print("Lista após pop():", lista)  # [40, 30, 15]

del lista[1]
print("Após del lista[1]:", lista)  # [40, 15]

lista.clear()
print("Após clear():", lista)  # []

# <<<<<DICAS E COMENTÁRIOS>>>>>
# append() - Adiciona um elemento ao final da lista
# insert(posição, valor) - Insere o valor em uma posição específica
# remove(valor) - Remove a primeira ocorrência do valor especificado
# sort() - Ordena a lista em ordem crescente
# reverse() - Inverte a ordem dos elementos da lista
# count(valor) - Conta quantas vezes o valor aparece na lista
# pop() - Remove e retorna o último elemento da lista
# del - Remove um elemento em uma posição específica
# clear() - Remove todos os elementos da lista
