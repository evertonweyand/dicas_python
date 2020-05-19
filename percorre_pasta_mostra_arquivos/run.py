import os

def lista_de_nomes_arquivos(pasta, extensao=''):
    arquivos = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]
    if extensao != '':
        arquivos = [arquivo for arquivo in arquivos if arquivo.lower().endswith(f'.{extensao}')]
    return arquivos


arquivos = lista_de_nomes_arquivos('.', 'txt') # . igual a pasta atual

for arq in arquivos:
    print(f'Arquivos: {arq}')