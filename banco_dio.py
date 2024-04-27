menu = """""
 Informe o serviço que você deseja executar:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0
limite = 1000
extrato = ""
numero_saque = 0
limite_saque = 5

while True:
    opcao = input (menu)
    if opcao == "d":
        valor = float(input("Qual valor você quer depositar?"))
        if valor > 0:
            saldo += valor
            extrato += f"Depóstio: R${valor:.2f}"
        else:
            print ("Operação falhou! O valor informado é inválido")   
    
    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar:"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saque > limite_saque

        if excedeu_saldo:
            print ("Operação falhou, saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou, O valor do saque excede o limite!")
        elif excedeu_saque:
            print("Operação falhou!Número máximo de saques excedidos.")  
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saque +=1
        else:
            print("Operação falhou, o valor informado não é valido.") 
    elif opcao == "e":
        print("\n ===========EXTRATO===========")
        print("Não foram realizados movimentações" if not extrato else extrato)
        print(f"\n Saldo: R${saldo:.2f}")
        print("================================")

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a opreação desejada.")    