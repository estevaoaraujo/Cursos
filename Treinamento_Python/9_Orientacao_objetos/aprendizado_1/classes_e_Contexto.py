# Definindo a classe ControleRemoto
class ControleRemoto:
    # Método construtor: é chamado automaticamente ao criar um novo objeto da classe
    def __init__(self, televisao, comodo):
        # Atributos do objeto: são armazenados na instância para uso posterior
        self.televisao = televisao      # Marca da televisão
        self.comodo = comodo            # Cômodo onde está a televisão

    # Método para simular o avanço de canal
    def avancar_canal(self):
        print('Canal avançado')  # Exibe mensagem indicando a ação

    # Método para simular o retorno ao canal anterior
    def voltar_canal(self):
        print('Voltar canal')  # Exibe mensagem indicando a ação

    # Método para escolher diretamente um canal
    def escolher_canal(self, canal):
        print('Alterado para o canal: {}'.format(canal))  # Mostra o canal escolhido


# Criando o primeiro objeto da classe ControleRemoto
controle_sala = ControleRemoto('LG', 'sala')  # TV da marca LG, localizada na sala

# Acessando e imprimindo os atributos do objeto
print(controle_sala.comodo)       # Mostra 'sala'
print(controle_sala.televisao)    # Mostra 'LG'

# Chamando métodos do objeto controle_sala
controle_sala.avancar_canal()     # Simula avançar canal
controle_sala.escolher_canal(20)  # Escolhe o canal 20


# Criando um segundo objeto da classe ControleRemoto
controle_quarto = ControleRemoto('Samsung', 'quarto')  # TV Samsung no quarto

# Acessando e imprimindo os atributos do segundo objeto
print(controle_quarto.comodo)       # Mostra 'quarto'
print(controle_quarto.televisao)    # Mostra 'Samsung'
