"""
#### Exercício 1

Receba três notas (números decimais) de um aluno e imprima a média.

Exemplo:

Digite a primeira nota:
8.5
Digite a segunda nota:
7.0
Digite a terceira nota:
9.0

Resposta:
Média: 8.17

Dica: Use inputs para receber os dados! 
Lembre de converter ele para o tipo necessário!
Print na tela com "print"
"""

Primeira_Nota = input("Insira sua primeira nota:")
Segunda_nota = input("Insira sua segunda nota:")
Terceira_nota = input("Insira sua terceira nota:")

Soma = (float(Primeira_Nota) + float(Segunda_nota) + float(Terceira_nota))
Média = Soma / 3
print(f"A média entre as suas notas é: {round(Média, 2)}") 
