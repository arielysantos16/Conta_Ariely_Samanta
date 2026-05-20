from conta import Conta 
obj_conta = Conta()
while True:
  opcao = int(input ("<3 Selecione o que deseja fazer:\n1-Saque\n2-Depositar\n3-Calcular Rendimento\n4-Sair"))
  if opcao == 1: 
    saque = int(input("Qual valor você deseja sacar?."))
    obj_conta.sacar(saque)
    mostrar = obj_conta.saldo
    print (f"Seu saldo atual após o saque é de R${mostrar}.")
  elif opcao == 2: 
    deposito = int(input("Qual valor você deseja depositar?."))
    obj_conta.depositar(deposito)
    mostrar = obj_conta.saldo
    print (f"Seu saldo atual após o depósito é de R${mostrar}.")
  elif opcao == 3: 
    mostrar = obj_conta.calcular_rendimento()
    print (f"Seu rendimento atual é de R${mostrar}.")
  elif opcao == 4: 
    break
  else:
    print ("Opção incorreta!!!")
