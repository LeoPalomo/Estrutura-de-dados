#  Um cliente adquiriu um restaurante e você foi contratado para desenvolver um programa em
#  Python que possibilite montar a tabela de preços dos produtos oferecidos, conforme o exemplo abaixo:

# 1 - Prato do dia: R$ 30,00
# 2 - Self-service por Quilo: R$ 35,00
# 3 - Refrigerante Lata 350ml: R$ 10,00
# 4 - Suco de Laranja/Uva/Abacaxi: R$ 10,00
# 5 - Água sem Gás 500ml: R$  3,00
# 6 - Água com Gás 500ml: R$  3,50
# 7 - Marmita Pequena: R$ 20,00
# 8 - Marmita Grande: R$ 30,00

# Utilize lista para armazenar e exibir os nomes e os valores dos produtos da tabela.

produtos = ['']*8
valores=[0]*8
print("Digite o nome e valor dos produtos")
for x in range(len(produtos)):
    produtos[x] = input(f"Digite o nome do {x+1} produto: ")
    valores[x]= float(input("Digite seu valor: "))
    print('\n')
print('\nProdutos')

for x in range(len(produtos)):
    print(f"Produto {produtos[x]} -- Valor: R${valores[x]}")

