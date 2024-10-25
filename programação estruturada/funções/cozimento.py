TEMPO_DE_ASSAR=40
def tempo_restante(x):
    if x > TEMPO_DE_ASSAR:
        print("A LASANHA QUEIMOU!")
    else:
        print("Faltam ",TEMPO_DE_ASSAR - x," minutos")

print("Cozimento da lasanha")
min_no_forno=int(input('Informe quanto tempo faz que a lasanha está no forno: '))

tempo_restante(min_no_forno)

def preparação(y):
    tempo=y*2
    print(f"Cada camada leva dois minutos. Você fez {y} camadas, totalizando {tempo} minutos de preparo")

numero_camadas=int(input("Informe quantas camadas você fará na lasanha: "))
preparação(numero_camadas)

