# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
"""
Este script solicita dois números ao usuário e realiza operações matemáticas básicas entre eles: soma, multiplicação, subtração e divisão.
Fluxo:
1. Solicita dois valores numéricos (float) via entrada padrão.
2. Calcula a soma, multiplicação, subtração e divisão dos valores informados.
3. Exibe os resultados das operações.
4. Para a divisão, verifica se o divisor é diferente de zero antes de realizar a operação, evitando erro de divisão por zero.
Entradas:
  - Primeiro valor (float)
  - Segundo valor (float)
Saídas:
  - Resultado da soma
  - Resultado da multiplicação
  - Resultado da subtração
  - Resultado da divisão (ou mensagem de erro se o divisor for zero)
"""

a = float(input("Primeiro valor:\n>"))
b = float(input("\nSegundo valor:\n>"))


soma = a + b
multiplicacao = a * b
subtr = a - b
divisao = a / b if b != 0 else None

print(f"Soma: {soma}")

print(f"Multiplicação: {multiplicacao}")

print(f"Subtração: {subtr}")
if divisao is not None:
    print(f"Divisão: {divisao}")
else:
    print("Divisão: impossível (divisor igual a zero)")
