import os
import shutil
from json import load, dump

arquivos = load(open('save.json', 'r'))
palavras_chave = load(open('palavras_chave.json', 'r'))

if arquivos['principal'] == None:
    local = input('digite o local que deseja organizar: ')
    arquivos['principal'] = local
    arquivos['zip'] = rf'{local}\zipados'
    arquivos['imagens'] = rf'{local}\imagem'
    arquivos['videos'] = rf'{local}\video'
    arquivos['documentos'] = rf'{local}\documentos'
    arquivos['musicas'] = rf'{local}\musicas'
    arquivos['executaveis'] = rf'{local}\executaveis'
    arquivos['outros'] = rf'{local}\outros'
    
    with open('save.json', 'w') as json_file:
        dump(arquivos, json_file, indent=4)

for caminho in arquivos.values():
    try:
        os.mkdir(caminho)
    except FileExistsError:
        continue

for root, dirs, files in os.walk(arquivos['principal']):
    for file in files:
        encontrado = False
        ext = file.split('.')[-1]

        for chave, valor in palavras_chave.items():
            if ext in valor:
                encontrado = True
                caminho_antigo = os.path.join(root, file)
                caminho_novo = os.path.join(arquivos[chave], file)
                shutil.move(caminho_antigo, caminho_novo)
                break
        
        if not encontrado:
            caminho_antigo = os.path.join(root, file)
            caminho_novo = os.path.join(arquivos['outros'], file)
            shutil.move(caminho_antigo, caminho_novo)

    print('organização concluida com sucesso')
    break