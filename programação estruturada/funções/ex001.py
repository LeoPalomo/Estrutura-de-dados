# def my_function():
#     print("My name is Leonardo")  #função simples sem o uso de argumentos
# my_function()

# def my_function(fnome):
#     print("My name is "+fnome)     #função usando argumento. Argumentos são informações passada para a função
# my_function("Leonardo")

# def my_function(*kid):
#     print("O mais novo é "+kid[1])         #argumentos arbitrários. Usamos o * quando não sabemos quantos
# my_function("João","Marcos","Jullio")       #argumentos serão passados para a função. A função receberá uma tupla de argumentos

# def my_function(child1, child3, child2):          #Função usando argumentos de palavra chave, tipo dicionário
#     print("The younger child is "+child2)        # ou seja, chave-valor
# my_function(child1='Enzo',child2="Marcelo",child3="Victor")         

# def my_function(country="Norway"):         #valor de parâmetro padrão. Caso chamamos a função sem argumento
#     print("My country is "+country)      #ela chamará o valor padrão
# my_function("Brazil")
# my_function("England")     
# my_function()


def my_function(food):         #Listas podem ser passadas como argumento(qualquer tipo de dado pode ser passado
    for x in food:             #como argumento)
        print(x)
fruits=['ameixa','melão','acerola']
my_function(fruits)

def my_function(x):         #Usamos a instrução return quando uma função retornar um valor
    return x*5
print(my_function(3))
print(my_function(10))    

def my_function(**kids):
    print("His last name is "+kids['lname'])   #usamos o ** se você não sabe quantos argumentos de palavra-chave
my_function(lname='pereira',fname='Luiz')      #tiver

def my_function(x):          #usamos a / (barra) para informar que os elementos antes dela são posicionais
    print(x)                   #caso não tenha isso, ele tem permissão de usar palavra-chave
my_function(3)

def my_function(x,y,/,*,a,b): #combinamos a / (barra) e o *(asterisco) para mesclar valores posicionais e de 
    print(a+b+x+y)           #palavras-chave
my_function(5,6,a=1,b=2)

