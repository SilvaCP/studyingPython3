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


# O código abaixo é PHP para uma comparação.
'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Dia da semana de nascimento</title>
</head>
<body>
    <form method="post">
        Mês de nascimento (1-12): <input type="number" name="mes" min="1" max="12" required><br>
        Ano de nascimento: <input type="number" name="ano" required><br>
        <input type="submit" value="Ver dia da semana">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $mes = $_POST["mes"];
        $ano = $_POST["ano"];

        // Cria a data com o primeiro dia do mês
        $data = "$ano-" . str_pad($mes, 2, "0", STR_PAD_LEFT) . "-01";

        // Pega o nome do dia da semana
        $dia_semana = date("l", strtotime($data));

        // Traduz para português
        $dias = [
            "Monday" => "Segunda-feira",
            "Tuesday" => "Terça-feira",
            "Wednesday" => "Quarta-feira",
            "Thursday" => "Quinta-feira",
            "Friday" => "Sexta-feira",
            "Saturday" => "Sábado",
            "Sunday" => "Domingo"
        ];

        echo "<p>O dia da semana do dia 1 de $mes/$ano foi: " . $dias[$dia_semana] . "</p>";
    }
    ?>
</body>
</html>

'''
