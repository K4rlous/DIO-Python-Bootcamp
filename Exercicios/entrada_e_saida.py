# Exemplo de operação de entrada e saída em Python
# Solicitando ao usuário que insira seu nome
nome = input("Por favor, insira seu nome: ")
print("Olá, " + nome + "! Bem-vindo ao programa.")

# Solicitando ao usuário que insira sua idade
idade = input("Por favor, insira sua idade: ")
print("Você tem " + idade + " anos.")

# Manipulação de print
nome = 'Carlos'
sobrenome = 'Rocha'

print(nome, sobrenome) # Carlos Rocha
print(nome, sobrenome, end="...\n") # Carlos Rocha...
# \n é o caractere de nova linha!
print(nome, sobrenome, sep="#") # Carlos#Rocha2