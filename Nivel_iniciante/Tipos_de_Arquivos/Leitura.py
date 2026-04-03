#O "r" é a função de leitura de arquivos txt.
arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()
