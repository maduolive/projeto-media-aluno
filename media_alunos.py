# media_alunos.py

# Entrada
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Processo
media = (nota1 + nota2 + nota3) / 3

# Saída
print(f"A média do aluno é: {media:.2f}")
if media > 6:
    print("Aprovado")
else:
    print("Reprovado")
if 5 < media <= 6:
    print("Recuperação")
elif media > 6:
    print("Aprovado")
else:
    print("Reprovado")
