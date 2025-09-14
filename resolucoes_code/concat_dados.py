# Vamos receber dois dados diferentes do usuário e concatena-los em uma única string?!
"""
Este script solicita ao usuário que insira seu primeiro e segundo nome,
concatena ambos em uma única string e exibe o nome completo formatado.
Fluxo:
1. Solicita o primeiro nome do usuário.
2. Solicita o segundo nome do usuário.
3. Concatena os nomes e exibe o resultado.
Uso:
Execute o script e siga as instruções no terminal para inserir os nomes.
"""


first_name = input("Insira seu Primeiro nome: \n >>")
last_name = input("\nInsira seu Segundo nome: \n >>")


print(f"\nSeu nome completo é: \n-> {first_name} {last_name}")
