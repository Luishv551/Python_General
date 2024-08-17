"""

Crie uma classe ContaBancaria que tenha os seguintes atributos:
* numero_conta
* saldo
E os seguintes métodos:
* depositar(valor): aumenta o saldo da conta.
* sacar(valor): diminui o saldo da conta, mas apenas se houver saldo suficiente.
* mostrar_saldo: exibe o saldo atual da conta.

"""
class ContaBancaria:

    def __init__(self, saldo=0) -> None:
        self.__saldo = saldo
    
    def mostrar_saldo(self) -> float:
        return self.__saldo
    
    def depositar(self, valor: float) -> None:
        self.__saldo += valor
    
    def sacar(self, valor: float) -> bool:
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            return False

minha_conta = ContaBancaria()

print(minha_conta.mostrar_saldo())

minha_conta.depositar(1000)
print(minha_conta.mostrar_saldo())

minha_conta.sacar(500)
print(minha_conta.mostrar_saldo())




        


        