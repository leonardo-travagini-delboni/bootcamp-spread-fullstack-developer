# Aplicacao do fluxograma do flowgorithm em python
# Autor: Leonardo Travagini Delboni

# Boas-vindas:
print('Bem-vindo ao programa de calculo de media!')

# Entrada de dados:
sair = False
lista = []

# Loop de entrada de dados para qualquer lenght de lista:
while not sair:
    ans = str(input("Deseja inserir uma nova nota? (s/n) "))
    if str(ans.lower())[0] == "n":
        sair = True
    else:
        nota = float(input("Digite uma nota: "))
        lista.append(nota)

# Processamento:
if len(lista) == 0:
    print('Muito obrigado!')
else:
    lista.sort()

    # Calculando a media da lista:
    media = (sum(lista) / len(lista)).__round__(2)

    # Calculando a mediana da lista:
    if len(lista) % 2 == 0:
        mediana = (lista[int(len(lista) / 2)] + lista[int(len(lista) / 2) - 1]) / 2
    else:
        mediana = lista[int(len(lista) / 2)]
    mediana = mediana.__round__(2)

    # Saida de dados:
    print("A media do aluno e: ", media)
    print("A mediana do aluno e: ", mediana)
    print('Muito obrigado!')