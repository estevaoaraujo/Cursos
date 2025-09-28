"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os   # Importa o módulo 'os' para poder usar comandos do sistema operacional (ex: limpar tela)

# Palavra que o jogador precisa descobrir
palavra_secreta = 'perfume'

# Variável que guarda as letras já acertadas pelo jogador
letras_acertadas = ''

# Conta quantas tentativas o jogador fez
numero_tentativas = 0

# Laço principal do jogo, roda indefinidamente até o jogador acertar
while True:
    # Pede para o jogador digitar uma letra
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1  # Cada vez que o jogador digita, conta como uma tentativa

    # Verifica se o jogador digitou mais de uma letra
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue  # Volta para o início do laço, sem processar a letra

    # Se a letra digitada estiver dentro da palavra secreta, adiciona às acertadas
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    # Monta a palavra parcial que o jogador já descobriu
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            # Se a letra já foi descoberta, mostra ela
            palavra_formada += letra_secreta
        else:
            # Se ainda não foi descoberta, mostra *
            palavra_formada += '*'

    # Mostra como está a palavra formada até agora
    print('Palavra formada:', palavra_formada)

    # Se o jogador acertou a palavra inteira
    if palavra_formada == palavra_secreta:
        os.system('clear')  # Limpa a tela (no Windows seria 'cls')
        print('VOCÊ GANHOU!! PARABÉNS!')
        print('A palavra era', palavra_secreta)
        print('Tentativas:', numero_tentativas)

        # Reseta variáveis para poder jogar de novo
        letras_acertadas = ''
        numero_tentativas = 0
