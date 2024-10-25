#  Crie um programa em Python que solicite ao usuário a inserção das notas de 5 alunos em uma lista. Para cada nota,
#  atribua um conceito de acordo com a tabela abaixo:
        # Nota >= 9: "A" 
        # Nota >= 7 e < 9: "B"        
        # Nota >= 5 e < 7: "C"
        # Nota < 5: "D"           
#Em seguida faça a exibição da lista de notas junto com os conceitos apresentados na tabela
z=0
nomes = 5 * [0]
while z < len(nomes):
    nomes[z]=input(f"Informe o nome do {z+1}º estudante: ")
    z+=1
print("\n")
notas=5*[0]
i=0
while i< len(notas):
    notas[i] = float(input(f"Informe a nota de {nomes[i]}: "))
    if notas[i] <0:
        print("Valor inválido!!")
        break
    i+=1
i=0
z=0
print("\n")
for x in notas:
    if notas[i] >= 9:
        print(f"{nomes[i]}: Nota = A  -- EXCELENTE")
    elif notas[i] >= 7 and notas[i]<=9:
         print(f"{nomes[i]}: Nota = B  -- ÓTIMO")
    elif notas[i] >= 5 and notas[i]<=7:
         print(f"{nomes[i]}: Nota = C -- REGULAR")
    else:
        print(f"{nomes[i]}: Nota = D -- INSATISFATÓRIO")
    i+=1

print("\n\n\n")
