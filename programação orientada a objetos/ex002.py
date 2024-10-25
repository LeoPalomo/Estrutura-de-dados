# 2. Crie uma classe chamada Retangulo que tenha dois atributos: largura e altura. A classe deve ter os
#  seguintes métodos:

# calcular_area_retangulo: calcula e retorna a área do retângulo.
# calcular_perimetro_retangulo: calcula e retorna o perímetro do retângulo.
print("-- Cálculo retângulo --\n")
class retangulo():
    def __init__(self,x,y):
        self.area = x*y
        self.perimetro=(2*x)+(2*y)
x=int(input("Informe o comprimento: "))
y=int(input("Informe a largura: "))
r=retangulo(x,y)
print("A área é: ", r.area)
print("O perímetro é: ",r.perimetro)