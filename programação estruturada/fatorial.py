#escreva um programa de fatorial usando laço for
resultado=1
fatorial=int(input("Insira um número: "))
for x in range(1,fatorial+1):
   print(x)
   resultado= resultado*x
   x=x+1
print(f"O fatorial de {fatorial}! é:{resultado} ")
