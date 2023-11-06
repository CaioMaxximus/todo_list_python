import json

# Abra o arquivo JSON para leitura
with open("../../db/data.json", "r") as arquivo_json:
    # Carregue o conteúdo JSON em uma lista de dicionários
    lista_de_objetos = json.load(arquivo_json)

# Agora você tem a lista de objetos em Python
for objeto in lista_de_objetos:
    print(objeto["nome"])
