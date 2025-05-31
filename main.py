'''
Esse é um comentário que pode ser de diversas linhas.
OK!
OK! Estudos de:
Operadores lógicos / e Condicionáis.
'''
# Primeiro exemplo.
'''
a = False #True
b = False
if a or b:
    print("Atendeu a condição!")
else:
    print("Não atendeu!")
'''
'''
# Segundo exemplo.
nome = "Filipe"
idade = 24
peso = 90
if idade == 25 and nome == "Filipe" and peso == 90: # !=25:
    print("Idade correta!")
else:
    print("Idade incorreta!")
'''

'''
import calendar

# Solicita ao usuário o mês e o ano
mes = int(input("Digite o mês de nascimento: "))
ano = int(input("Digite o ano de nascimento: "))

# Define o dia 1 do mês e ano fornecidos
dia_da_semana = calendar.weekday(ano, mes, 1)

# Lista com nomes dos dias da semana
dias = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

# Exibe o resultado
print(f"O dia da semana do seu nascimento foi: {dias[dia_da_semana]}")

'''
print(2030)
