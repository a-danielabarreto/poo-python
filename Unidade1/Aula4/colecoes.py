# conjuntos (não posso alterar o valor)
conjunto = set([4, 7, 2, 3, 0, 8])
print("Conjunto: ", conjunto)

# tupla (também não posso alterar o valor)
tupla = (3, 2, 4, 6, 0)
print("Tupla: ", tupla)

# dicionário
pessoa = {"nome": "Daniela", "telefone": "(61) 98765-4321", "endereço": "ABC"}
print(pessoa["nome"])

pessoas = [
    {"nome": "Daniela", "telefone": "(61) 98765-4321", "endereço": "ABC"},
    {"nome": "Maria", "telefone": "(61) 98888-4321", "endereço": "DEF"},
    {"nome": "João", "telefone": "(61) 98877-4321", "endereço": "GHI"},
    {"nome": "Antônio", "telefone": "(61) 98866-4321", "endereço": "JKL"}
]

print(pessoas[0])
print(pessoas[0]["nome"])