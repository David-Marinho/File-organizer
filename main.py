import os
import shutil

local = input('digite o local que deseja organizar: ')

dir = [rf'{local}\imagens', rf'{local}\zipados', rf'{local}\executaveis', rf'{local}\documentos', rf'{local}\outros']
palavras_chave = {'imagens': ['png', 'jpg', 'webp'], 'zipados': ['zip', 'rar'], 'executaveis': ['exe'], 'documentos': ['docx', 'pdf']}

for caminho in dir:
    try:
        os.mkdir(caminho)
    except FileExistsError:
        continue

for root, dirs, files in os.walk(local):
    for file in files:
        ext = file.split('.')[-1]

        if ext in palavras_chave['imagens']:
            caminho_antigo = os.path.join(root, file)
            caminho_novo = os.path.join(dir[0], file)  
            shutil.move(caminho_antigo, caminho_novo)
        
        elif ext in palavras_chave['zipados']:
            caminho_antigo = os.path.join(root, file)
            caminho_novo = os.path.join(dir[1], file)  
            shutil.move(caminho_antigo, caminho_novo)
        
        elif ext in palavras_chave['executaveis']:
            caminho_antigo = os.path.join(root, file)
            caminho_novo = os.path.join(dir[2], file)  
            shutil.move(caminho_antigo, caminho_novo)
        
        elif ext in palavras_chave['documentos']:
            print(f'{ext} é um documento')
            caminho_antigo = os.path.join(root, file)
            caminho_novo = os.path.join(dir[3], file)  
            shutil.move(caminho_antigo, caminho_novo)
        
        else:
            caminho_antigo = os.path.join(root, file)
            caminho_novo = os.path.join(dir[4], file)  
            shutil.move(caminho_antigo, caminho_novo)
    break

print('organização concluida com sucesso')