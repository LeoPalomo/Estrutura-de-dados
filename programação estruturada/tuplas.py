thistuple=('maça','banana','laranja')
print(len(thistuple))
print(type(thistuple))
print(thistuple[0])

#tuplas são imutáveis, ou seja, para adicionar um membro a ela será necessária soluções alternativas
y=list(thistuple)
y.append("cherry")
thistuple=tuple(y)
print(thistuple)

(a,b,c,d) = thistuple;
print(b)

for x in thistuple:
    print(x)
mytuple=('yellow',)
joinTuple=thistuple+mytuple
print(joinTuple)