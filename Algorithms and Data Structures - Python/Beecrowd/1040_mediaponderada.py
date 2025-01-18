
A,B,C,D = map(float, input().split())

media = ((A * 2) + (B * 3) + (C * 4) + (D * 1)) / 10
print(f"Media: {media:.1f}")

if media >= 7:
    print("Aluno aprovado.")
if media < 5:
    print("Aluno reprovado.")

if media >= 5 and media <= 6.9:
    print("Aluno em exame")

    nota_exame = float(input())

    print(f"Nota do exame: {nota_exame:.1f}")

    media_final = (media + nota_exame) / 2

    if media >= 5:
        print("Aluno aprovado.")
        print(f"Media final: {media_final:.1f}")



