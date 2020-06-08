frutas = ("Platano", "Mango", "Guayaba", "Pina")

print(len(frutas))
print(frutas[0])
print(frutas[-2])
print(frutas[0:2])
print(frutas[:3])
print(frutas[3:])

listaFrutas = list(frutas);
print(listaFrutas)

for f in frutas:
    print(f, end=", ")
