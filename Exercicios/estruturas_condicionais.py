MAIOR_IDADE = 18
SALDO = 1000.0

idade = int(input("Digite sua idade: "))


if idade >= MAIOR_IDADE:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

valor_saque = float(input("Digite o valor que deseja sacar: "))
if valor_saque <= SALDO:
    SALDO -= valor_saque
    print(f"Saque realizado com sucesso! Saldo restante: R${SALDO:.2f}")
else:
    print("Saldo insuficiente para realizar o saque.")
    
# IF TERNÁRIO
mensagem = "Maior de idade" if idade >= MAIOR_IDADE else "Menor de idade"
print(mensagem)