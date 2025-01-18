"""
Tesoura corta papel
Papel cobre pedra
Pedra derruba lagarto
Lagarto adormece Spock
Spock derrete tesoura
Tesoura prende lagarto
Lagarto come papel
Papel refuta Spock
Spock vaporiza pedra
Pedra quebra tesoura
"""

#REGRAS DA VITORIA 
tesoura = ["papel", "lagarto"]
papel = ["pedra", "spock"]
pedra = ["lagarto", "tesoura"]
lagarto = ["spock", "papel"]
spock = ["tesoura", "pedra"]

def determinar_vencedor(rajesh, sheldon):
    
    if rajesh == sheldon:
        return "empate"
    
    if rajesh == "tesoura" and sheldon in tesoura:
        return "rajesh"
    elif rajesh == "papel" and sheldon in papel:
        return "rajesh"
    elif rajesh == "pedra" and sheldon in pedra:
        return "rajesh"
    elif rajesh == "lagarto" and sheldon in lagarto:
        return "rajesh"
    elif rajesh == "spock" and sheldon in spock:
        return "rajesh"
    else:
        return "sheldon"


n_partidas = int(input())


for _ in range(n_partidas):

    rajesh, sheldon = input().split()
    
    resultado = determinar_vencedor(rajesh, sheldon)

    print(resultado)

"""

# REGRAS DA VITORIA
regras_vitoria = {
    "tesoura": ["papel", "lagarto"],
    "papel": ["pedra", "spock"],
    "pedra": ["lagarto", "tesoura"],
    "lagarto": ["spock", "papel"],
    "spock": ["tesoura", "pedra"]
}

def determinar_vencedor(rajesh, sheldon):
    if rajesh == sheldon:
        return "empate"
    elif sheldon in regras_vitoria[rajesh]:
        return "rajesh"
    else:
        return "sheldon"

n_partidas = int(input())

for _ in range(n_partidas):
    rajesh, sheldon = input().split()
    resultado = determinar_vencedor(rajesh, sheldon)
    print(resultado)


"""
