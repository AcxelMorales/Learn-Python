diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Orientd Programming",
    "DBMS": "Database Management System"
}

print(diccionario)
print(len(diccionario))
print(diccionario["IDE"])
print(diccionario.get("OOP"))

for key in diccionario:
    print(key)

for key in diccionario:
    print(diccionario[key])

for value in diccionario.values():
    print(value)
