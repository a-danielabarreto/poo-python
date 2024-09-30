# arquivo = open("pessoas.txt", "w") w: escreve substituindo

arquivo = open("pessoas.txt", "a+") #a+: escreve adicionando

arquivo.write("João\n")
arquivo.write("Daniela\n")
arquivo.write("Maria\n")

arquivo.close()

with open("pessoas.txt", "r+") as arquivoLeitura:
    
    for linha in arquivoLeitura:
        print(linha)

