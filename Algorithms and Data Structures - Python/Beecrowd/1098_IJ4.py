"""

I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?

LOGICA:

A SEQUENCIA VAI COMECAR COM O 0 E O J SENDO 0 + 1 A CADA REPETICAO NESSE BLOCO DE 3 REPETICOES

FEITO ISSO SERA SOMADO 0.2 A CADA 3 REPETICOES DESSA, ATE CHEGAR NO I = 2   


"""


I = 0

while I <= 2:

    for j in range(3):

        J = I + 1 + j

        # Formatar I e J para que inteiros não tenham casas decimais
        I_formatted = int(I) if I == int(I) else f"{I:.1f}"
        J_formatted = int(J) if J == int(J) else f"{J:.1f}"

        print(f"I={I_formatted} J={J_formatted}")
        
    I = round(I + 0.2, 1)






