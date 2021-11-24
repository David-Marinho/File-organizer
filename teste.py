dicio = {'palavras': ['teste', 'alo'], 'numeros': ['0', '1', '2']}

coisa = str(input('digite algo: ')).split('.')

if coisa[1] in dicio['palavras']:
    print('palavra')

if coisa[1] in dicio['numeros']:
    print('numero')