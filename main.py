from conta import Conta 
obj_conta = Conta()
opcao = int(input (" <3 Selecione o que deseja fazer:\n 1-Saque\n 2-Depositar\n 3-Calcular Rendimento"))
if opcao == 1: 
  saque = int(input("Qual valor você deseja sacar?"))
  obj_conta.sacar(saque)
  mostrar = obj_conta.saldo
  print ("Seu sal")
