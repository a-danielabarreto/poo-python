import json

pessoas = [
    {"nome": "Daniela", "telefone": "(83) 98988-7070", "endereco": "ABC"},
    {"nome": "Maria", "telefone": "(83) 98000-2121", "endereco": "DEF"},
    {"nome": "Joao", "telefone": "(83) 99000-1010", "endereco": "GHI"}
]

with open("pessoas.json", "w") as arquivo:
    json.dump(pessoas, arquivo, indent=4)