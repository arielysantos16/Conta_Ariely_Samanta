Class Conta:
  def __init__(self):
    self.saldo = 0

  def sacar(self, valor_saque):
    self.saldo -= valor_saque
    return self.saldo
    
  def depositar(self, valor_deposito):
    self.saldo += valor_deposito
    return self.saldo
    
  def calcular_rendimento(self):
    rendimento = self.saldo * 0.1
    return rendimento
