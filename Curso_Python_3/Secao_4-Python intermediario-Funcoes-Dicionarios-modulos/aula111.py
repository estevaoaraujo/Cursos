perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


for pergunta in perguntas:
    print(pergunta['Pergunta'])
    for opcao in pergunta['Opções']:
        print(opcao)
    resposta_usuario = input('Resposta: ')
    if resposta_usuario == pergunta['Resposta']:
        print('Resposta correta!')
    else:
        print('Resposta incorreta!')
