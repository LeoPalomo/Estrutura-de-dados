# 3. Elabore um programa em Python para uma loja de tintas, onde
# o programa deverá solicitar ao funcionário o tamanho em metros quadrados da área a ser pintada.
# Sendo que a cobertura da tinta é de 170 metros quadrados para as latas de 
# 18 litros e que cada lata custa R$ 480,00. Calcule e mostre a quantidade de latas de tinta a serem compradas e 
# o preço total.
import math

tamanho=float(input("Informe a área a ser pintada(em M²): "))
cobertura_unidade_lata = 170.0
latas=tamanho/cobertura_unidade_lata
arredondamento=math.ceil(latas) #arredondar a quantidade de latas, para cima
print(f"\nSerão necessárias {arredondamento} latas de 18 litros. E irá sobrar {(arredondamento-latas)*18} litros")
preço=480.00*arredondamento
print("O valor total é %.2f"%preço)