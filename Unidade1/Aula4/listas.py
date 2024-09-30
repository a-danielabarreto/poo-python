numeros = [10, 20, 30, 17, 58, 3, 7]
print(numeros)
print(numeros[0])

carros = ["Pálio", "Gol", "Virtus", "Ka", "Onix"]
print(carros)
print(carros[2])
print(len(carros))

carros.append("Kombi")
print(carros)
print(len(carros))

carros.remove("Gol")
print(carros)
print(len(carros))

del carros[0]
print(carros)
print(len(carros))

carros = sorted(carros)
print(carros)

for carro in carros:
    print(carro)