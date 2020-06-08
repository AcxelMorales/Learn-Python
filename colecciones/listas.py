nombres = ["Juan", "Pedro", "Liz", "Sofia"]

print(nombres)
print(len(nombres))
print(nombres[0])
print(nombres[-2])
print(nombres[0:2])
print(nombres[:3])
print(nombres[3:])

nombres.append("Nuevo 1")
nombres.pop()
nombres.insert(1, "Nuevo 2")
nombres.remove("Nuevo 2")

del nombres[0]

for i in nombres:
    print(i)

if "Liz" in nombres:
    print("Existe")
else:
    print("No existe")
