'''# Definindo a classe Pessoa
class Pessoa:
    # Método construtor (__init__) chamado ao criar um novo objeto
    def __init__(self, nome, idade, cpf):
        # Atributos privados (com dois underlines '__'): não devem ser acessados diretamente de fora da classe
        self.__nome = nome    # Nome da pessoa (privado)
        self.__idade = idade  # Idade da pessoa (privado)
        self.__cpf = cpf      # CPF da pessoa (privado)

    # Método público: qualquer parte do código pode chamar este método
    def correr(self):
        print('Estou correndo')  # Exibe mensagem ao correr

    # Método público com parâmetro 'bebida'
    def beber(self, bebida):
        # Se a bebida for 'cerveja', exige apresentar o documento
        if bebida == 'cerveja':
            self.__apresenta_documento()  # Método privado chamado internamente
        print('bebendo...')  # Exibe mensagem comum a qualquer bebida

    # Método privado: só pode ser usado dentro da classe
    def __apresenta_documento(self):
        print(self.__cpf)  # Exibe o CPF da pessoa (simulando apresentação de documento)


# Criando uma instância da classe Pessoa
nome = Pessoa('ronaldo', 32 , '085.254.522')

# Chamando o método beber com 'cerveja': exige documento
nome.beber('cerveja')

# Chamando o método beber com 'coca_cola': não exige documento
nome.beber('coca_cola')
'''


# Definição da classe Calculadora
class Calculadora:

    # Método principal que escolhe a operação
    def calcular(self, op, num1, num2):
        if op == '+':
            return self.__adicionar(num1, num2)  # Chama o método privado de adição
        elif op == '-':
            return self.__subtrair(num1, num2)   # Chama o método privado de subtração
        else:
            print('Operação Inválida')  # Caso o operador não seja reconhecido

    # Método privado para somar dois números
    def __adicionar(self, num1, num2):
        return num1 + num2

    # Método privado para subtrair dois números
    def __subtrair(self, num1, num2):
        return num1 - num2

# Criação de um objeto da classe Calculadora
calculadora = Calculadora()

# Chamando o método calcular com operador de soma
resultado = calculadora.calcular('+', 3, 2)

# Exibindo o resultado
print(resultado)


