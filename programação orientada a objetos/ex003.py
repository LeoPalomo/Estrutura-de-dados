# 3. Crie uma classe chamada Veiculo com os seguintes atributos:

# marca: marca do veículo.
# modelo: modelo do veículo.
# ano: ano de fabricação.
# velocidade: a velocidade atual do veículo (inicialmente 0 (zero)).

# Crie também os seguintes métodos:

# acelerar: aumenta a velocidade do veículo em 5 km/h.
# frear: reduz a velocidade do veículo em 5 km/h (a velocidade mínima é 0 km/h).
# exibir_informacoes: exibe a marca, modelo, ano e velocidade atual do veículo.


class veiculo:
    def __init__(self,marca,modelo,ano,velocidade):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.velocidade=velocidade
    
    def acelerar(self):
        self.aceleração=self.velocidade*1.05
        print("Acelerando chegamos a ", self.aceleração,"km/h")
    
    def frear(self):
        self.freio=self.velocidade * 0.95
        print("Freiando chegamos a ",self.freio,"km/h")

    def exibir_informações(self):
        print(carro.marca,carro.modelo,carro.ano,carro.velocidade,"km/h")

carro=veiculo("Ford","Mustang","1979",180)


carro.acelerar()
print("\n")
carro.frear()
print("\n")
carro.exibir_informações()


