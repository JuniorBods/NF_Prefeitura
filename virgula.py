import os

# Caminho da pasta que queremos verificar
caminho_da_pasta = "caminho/para/a/pasta"

# Verifica se a pasta existe
if not os.path.exists(caminho_da_pasta):
    # Cria a pasta
    os.makedirs(caminho_da_pasta)
    print("Pasta criada com sucesso!")
else:
    print("A pasta já existe.")