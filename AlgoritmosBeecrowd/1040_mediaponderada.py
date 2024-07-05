import sys

def calcula_media_pond(n1, n2, n3, n4, exame_nota):
    m = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4)) / 10
    return m, exame_nota

def verifica_aprovacao1(m):
    if m >= 7:
        return "Aluno aprovado."
    return "Aluno em exame."

def exame(exame_nota, m):
    nova_media = (exame_nota + m) / 2
    if nova_media >= 5:
        return "Aluno aprovado.", nova_media
    return "Aluno reprovado.", nova_media

m, exame_nota = calcula_media_pond(2, 4, 7.5, 8, 6.4)

print(f"Media: {m}")
status = verifica_aprovacao1(m)
print(status)

if status == "Aluno aprovado.":
    sys.exit()
    pass

print(f"Nota do exame: {exame_nota}")

status, nova_media = exame(exame_nota, m)

print(status)
print(f"Media final: {nova_media}")


"""
#SOLUCAO ELEGANTE:

# Função para calcular a média ponderada
def calcula_media_pond(n1, n2, n3, n4):
    media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
    return media

# Função principal que executa a lógica do problema
def main():
    # Leitura das quatro notas
    n1, n2, n3, n4 = map(float, input().split())
    
    # Calcular a média ponderada
    media = calcula_media_pond(n1, n2, n3, n4)
    
    # Imprimir a média com uma casa decimal
    print(f"Media: {media:.1f}")
    
    # Verificação das condições de aprovação, exame ou reprovação
    if media >= 7.0:
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        
        # Leitura da nota do exame
        exame_nota = float(input())
        print(f"Nota do exame: {exame_nota:.1f}")
        
        # Recalcular a média com a nota do exame
        media_final = (media + exame_nota) / 2
        
        # Verificação da condição após o exame
        if media_final >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        
        # Imprimir a média final com uma casa decimal
        print(f"Media final: {media_final:.1f}")

# Chamada da função principal
if __name__ == "__main__":
    main()

"""
