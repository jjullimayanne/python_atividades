from re import A

# palavra reservada class seguida do nome da class


class Calculadora:
    # criar método com a palavra reservada def e construtor com a palavra reservada __init__
    # passa os atributos da classe
    def __init__(self, numeroUm, numeroDois) -> None:
        # vamos receber esse valor sempre que esse objeto for instanciado
        self.numeroUm = numeroUm
        self.numeroDois = numeroDois
    # método de somar

    def somar(self):
        return self.numeroUm + self.numeroDois
    # método de subtrair

    def subtrair(self):
        return self.numeroUm - self.numeroDois
    # método de dividir

    def dividir(self):
        return self.numeroUm / self.numeroDois
    # método de multiplicar

    def multiplicar(self):
        return self.numeroUm * self.numeroDois
    # método de exponenciação

    def exponenciação(self):
        return self.numeroUm ** self.numeroDois
    # método de modulo

    def modulo(self):
        return self.numeroUm % self.numeroDois


# receber os numeros por input
numeroUm = int(input("Digite o primeiro número para o calculo: "))
numeroDois = int(input("Digite o segundo número para o calculo: "))
# receber escolha da operação por input
escolhaOperacao = int(input(
    "Digite o numero correspondente a operação que deseja fazer: \n 1) Soma \n 2) Subtração \n 3) Multiplicação \n 4) Divisão \n 5) Exponenciação \n 6) Módulo \n "))

conta = Calculadora(numeroUm, numeroDois)

# fazer a operação de acordo com o input recebido
if escolhaOperacao == 1:
    print(f'O resultado da operação é {conta.somar()}')
elif escolhaOperacao == 2:
    print(f'O resultado da operação é {conta.subtrair()}')
elif escolhaOperacao == 3:
    print(f'O resultado da operação é {conta.multiplicar()}')
elif escolhaOperacao == 4:
    print(f'O resultado da operação é {conta.dividir()}')
elif escolhaOperacao == 5:
    print(f'O resultado da operação é {conta.exponenciação()}')
elif escolhaOperacao == 6:
    print(f'O resultado da operação é {conta.modulo()}')
