# 4. Elabore um programa em Python que solicite ao usuário que insira 10 números inteiros e 
# os armazene em uma lista, em seguida verifique quais números da lista são primos e faça a exibição da 
# quantidade encontrada e de todos os números primos.
i=0
lista = 10*[0]
name = input("Insira o seu nome: ")
print(f"Olá {name}. Informe 10 números:")
while i < 10:
    lista[i] = int(input())
    i+=1
y=1

numeros = [] # Lista vazia
primos = [] # Lista vazia
cont = 0 
num = 0

def primo(num): #
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)
    if primo(num): # Utiliza a função criada para verificação
        primos.append(num)
        cont += 1

print(f"Quantidade de Números Primos digitada: {cont}\nPrimos: {primos}")

