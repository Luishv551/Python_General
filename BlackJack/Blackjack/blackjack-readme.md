# Jogo de Blackjack em Python

Este é um simples jogo de Blackjack implementado em Python usando PyQt5 para a interface gráfica do usuário.

## Descrição

Este projeto implementa as regras básicas do Blackjack (também conhecido como 21) em uma interface gráfica de usuário simples e intuitiva. O jogo permite que o jogador faça apostas, receba cartas, e jogue contra um dealer controlado pelo computador.

## Características

- Interface gráfica usando PyQt5
- Implementação das regras básicas do Blackjack
- Sistema de apostas
- Decisões de "Hit" e "Stand"
- Lógica do dealer automática
- Detecção de Blackjack e pagamento de 3:2
- Gerenciamento de orçamento do jogador

## Requisitos

- Python 3.6+
- PyQt5

## Instalação

1. Certifique-se de ter Python instalado em seu sistema.
2. Instale o PyQt5 usando pip:

```
pip install PyQt5
```

3. Clone este repositório ou baixe o arquivo `blackjack_game.py`.

## Como Jogar

1. Execute o script Python:

```
python blackjack_game.py
```

2. A interface do jogo será aberta.
3. Insira sua aposta no campo "Aposta" e clique em "Apostar".
4. Use os botões "Hit" para pedir mais cartas ou "Stand" para manter sua mão atual.
5. O dealer jogará automaticamente após você terminar sua jogada.
6. O resultado da rodada será exibido e seu orçamento será atualizado.
7. Clique em "Novo Jogo" para iniciar uma nova rodada.

## Regras Básicas

- O objetivo é ter uma mão com valor mais próximo de 21 do que a mão do dealer, sem ultrapassar 21.
- Cartas numéricas valem seu valor nominal, figuras (J, Q, K) valem 10, e Ases podem valer 1 ou 11.
- Um "Blackjack" (um Ás e uma carta de 10 pontos) paga 3:2.
- O dealer deve "Hit" em 16 e "Stand" em 17.

## Contribuições

Contribuições para melhorar o jogo são bem-vindas. Sinta-se à vontade para fazer um fork do repositório e enviar pull requests.



