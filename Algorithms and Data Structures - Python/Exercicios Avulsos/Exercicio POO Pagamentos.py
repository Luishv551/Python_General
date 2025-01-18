from abc import ABC, abstractmethod
import random

class Pagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, numero, limite):
        self.numero = numero
        self.limite = limite

    def pagar(self, valor):
        if len(str(self.numero)) != 16:
            return "Falha: Número do cartão inválido"
        if valor > self.limite:
            return "Falha: Limite de crédito excedido"
        if random.random() < 0.1:  # 10% de chance de falha
            return "Falha: Transação não autorizada"
        self.limite -= valor
        return f"Sucesso: Pagamento de R${valor:.2f} realizado com Cartão de Crédito"

class PayPal(Pagamento):

    _usuarios = {
        "usuario@email.com": {"senha": "senha123", "saldo": 1000},
        "outro@email.com": {"senha": "outrasenha", "saldo": 500}
    }

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.saldo = None 

    def pagar(self, valor):
        if not self._verificar_credenciais():
            return "Falha: Credenciais inválidas"
        if self.saldo is None:
            return "Falha: Faça login primeiro"
        if valor > self.saldo:
            return "Falha: Saldo insuficiente"
        if random.random() < 0.05:  # 5% de chance de falha
            return "Falha: Erro na transação"
        self.saldo -= valor
        self._usuarios[self.email]["saldo"] = self.saldo
        return f"Sucesso: Pagamento de R${valor:.2f} realizado com PayPal"

    def _verificar_credenciais(self):
        if self.email in self._usuarios and self._usuarios[self.email]["senha"] == self.senha:
            self.saldo = self._usuarios[self.email]["saldo"]
            return True
        return False


if __name__ == "__main__":

    # Teste com Cartão de Crédito
    cartao = CartaoCredito(1234567890123456, 1000) #Numero e Limite
    print(cartao.pagar(500))
    print(cartao.pagar(900))
    print(cartao.pagar(200))

    # Teste com PayPal (credenciais válidas)
    paypal = PayPal("usuario@email.com", "senha123")
    print(paypal.pagar(500))
    print(paypal.pagar(800))
    print(paypal.pagar(400))

    # Teste com PayPal (credenciais inválidas)
    paypal_invalido = PayPal("usuario@email.com", "senhaerrada")
    print(paypal_invalido.pagar(100))

    # Teste com número de cartão inválido
    cartao_invalido = CartaoCredito(12345, 1000)
    print(cartao_invalido.pagar(100))