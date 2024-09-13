import PySimpleGUI as sg
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
budget = 100

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
    return hand

def total(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 21
    if 11 in hand and sum(hand) > 21:
        hand[hand.index(11)] = 1
    return sum(hand)

def hit(hand):
    card = deck.pop()
    hand.append(card)
    return hand

def clear(hand):
    while total(hand) < 17:
        hit(hand)
    return hand

def create_window():
    layout = [
        [sg.Text('Orçamento: '), sg.Text('100', key='-BUDGET-')],
        [sg.Text('Aposta: '), sg.Input(key='-BET-', size=(10, 1)), sg.Button('Apostar')],
        [sg.Text('Mão do jogador: '), sg.Text('', key='-PLAYER-HAND-')],
        [sg.Text('Total do jogador: '), sg.Text('', key='-PLAYER-TOTAL-')],
        [sg.Text('Mão do dealer: '), sg.Text('', key='-DEALER-HAND-')],
        [sg.Text('Total do dealer: '), sg.Text('', key='-DEALER-TOTAL-')],
        [sg.Button('Hit'), sg.Button('Stand')],
        [sg.Text('', key='-MESSAGE-')],
        [sg.Button('Novo Jogo'), sg.Button('Sair')]
    ]
    return sg.Window('Blackjack', layout, finalize=True)

def update_window(window, player_hand, dealer_hand, show_player=True, show_dealer=False):
    if show_player:
        window['-PLAYER-HAND-'].update(player_hand)
        window['-PLAYER-TOTAL-'].update(total(player_hand))
    else:
        window['-PLAYER-HAND-'].update('*****')
        window['-PLAYER-TOTAL-'].update('*')
    
    if show_dealer:
        window['-DEALER-HAND-'].update(dealer_hand)
        window['-DEALER-TOTAL-'].update(total(dealer_hand))
    elif dealer_hand:
        window['-DEALER-HAND-'].update([dealer_hand[0], '*'])
        window['-DEALER-TOTAL-'].update(dealer_hand[0])
    else:
        window['-DEALER-HAND-'].update('*****')
        window['-DEALER-TOTAL-'].update('*')

def reset_game_state(window):
    global deck
    if len(deck) < 20:
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    update_window(window, [], [], show_player=False, show_dealer=False)
    window['-BET-'].update('')
    window['-MESSAGE-'].update('')
    window['Apostar'].update(disabled=False)
    window['Hit'].update(disabled=True)
    window['Stand'].update(disabled=True)

def game(window):
    global budget, deck
    
    reset_game_state(window)
    
    while True:
        event, values = window.read()
        
        if event in (sg.WINDOW_CLOSED, 'Sair'):
            return False
        
        if event == 'Apostar':
            try:
                bet = int(values['-BET-'])
                if 0 < bet <= budget:
                    window['Apostar'].update(disabled=True)
                    window['Hit'].update(disabled=False)
                    window['Stand'].update(disabled=False)
                    break
                else:
                    window['-MESSAGE-'].update('Aposta inválida!')
            except ValueError:
                window['-MESSAGE-'].update('Por favor, insira um número válido!')
    
    player_hand = deal(deck)
    dealer_hand = deal(deck)
    update_window(window, player_hand, dealer_hand)
    
    if total(player_hand) == 21:
        budget += bet * 1.5
        window['-MESSAGE-'].update('Blackjack! Você ganhou 1.5x a aposta!')
        window['-BUDGET-'].update(budget)
        update_window(window, player_hand, dealer_hand, show_dealer=True)
        return True
    
    while True:
        event, values = window.read()
        
        if event in (sg.WINDOW_CLOSED, 'Sair'):
            return False
        
        if event == 'Hit':
            player_hand = hit(player_hand)
            update_window(window, player_hand, dealer_hand)
            if total(player_hand) > 21:
                budget -= bet
                window['-MESSAGE-'].update('Você estourou! Dealer ganha!')
                window['-BUDGET-'].update(budget)
                update_window(window, player_hand, dealer_hand, show_dealer=True)
                return True
        
        if event == 'Stand':
            break
    
    dealer_hand = clear(dealer_hand)
    update_window(window, player_hand, dealer_hand, show_dealer=True)
    
    player_score = total(player_hand)
    dealer_score = total(dealer_hand)
    
    if dealer_score > 21:
        budget += bet
        window['-MESSAGE-'].update('Dealer estourou! Você ganhou!')
    elif player_score > dealer_score:
        budget += bet
        window['-MESSAGE-'].update('Você ganhou!')
    elif dealer_score > player_score:
        budget -= bet
        window['-MESSAGE-'].update('Dealer ganhou!')
    else:
        window['-MESSAGE-'].update('Empate!')
    
    window['-BUDGET-'].update(budget)
    return True

def main():
    window = create_window()
    
    while True:
        if not game(window):
            break
        
        if budget <= 0:
            sg.popup('Você ficou sem dinheiro! Fim de jogo.')
            break
        
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Sair'):
            break
        if event != 'Novo Jogo':
            break
    
    window.close()

if __name__ == '__main__':
    main()