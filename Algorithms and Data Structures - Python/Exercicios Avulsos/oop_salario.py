"""
1) Crie uma classe Funcionario que tenha os seguintes atributos:
* nome
* salario
E os seguintes métodos:
* aumentar_salario(percentual): aumenta o salário em uma porcentagem dada.
* mostrar_informacoes: imprime o nome e o salário do funcionário.
"""

class Funcionario:

    def __init__(self, nome, salario=0) -> None:
        self.nome = nome
        self.salario = salario
    
    def aumentar_salario(self, perc: float) -> None:
        self.salario = self.salario * (1 + (perc / 100))

    def mostrar_informacoes(self) -> str:
        return f"Nome: {self.nome}, Salário: {self.salario:.2f}"

Funcionario = Funcionario("Luis", 1000)

Funcionario.aumentar_salario(10)

print(Funcionario.mostrar_informacoes())
    

