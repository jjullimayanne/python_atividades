from re import A

#palavra reservada class seguida do nome da class
class Calculadora:
    # criar metodo com a palavra reservada def e construtor com a palavra reservada __init__
    #passa os atributos da classe
    def __init__(self, numeroUm, numeroDois) -> None:
        #vamos receber esse valor sempre que esse objeto for instanciado
        self.numeroUm = numeroUm
        self.numeroDois = numeroDois
    # metodo de somar 
    def somar(self):
        return self.numeroUm + self.numeroDois
    #metodo de subtrair
    def subtrair(self):
        return self.numeroUm - self.numeroDois
    #metodo de dividir
    def dividir(self):
        return self.numeroUm / self.numeroDois
    #meotodo de multiplicar 
    def multiplicar(self):
        return self.numeroUm * self.numeroDois
    #meotodo de exponenciação
    def exponenciação(self):
         return self.numeroUm ^ self.numeroDois
    #meotodo de modulo
    def modulo(self):
         return self.numeroUm % self.numeroDois
        
 #receber os numeros por input
numeroUm = int(input("Digite o primeiro número para o calculo: "))
numeroDois = int(input("Digite o segundo número para o calculo: "))
 #receber escolha da operação por input
escolhaOperacao = int(input("Digite o numero correspondente a operação que deseja fazer: \n 1) Soma \n 2) Subtraçao \n 3) Multiplicação \n 4) Divisão \n 5) Exponenciação \n 6) Divisão \n "))

conta = Calculadora(numeroUm, numeroDois)

#fazer a operação de acordo com o input recebido
if escolhaOperacao == 1:
    print(conta.somar())
elif escolhaOperacao == 2:
    print(conta.subtrair())
elif escolhaOperacao == 3:
    print(conta.multiplicar())
elif escolhaOperacao == 4:
    print(conta.dividir())
elif escolhaOperacao == 5:
    print(conta.exponenciação())
elif escolhaOperacao == 6:
    print(conta.modulo())


