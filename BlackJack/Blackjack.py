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
    if sum(hand) == 21:
        return 21
    elif 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
        return sum(hand)
    else:
        return sum(hand)

def hit(hand):
    card = deck.pop()
    hand.append(card)
    return hand

def clear(hand):
    if total(hand) < 17:
        hit(hand)
    return hand

def game():
    global budget
    player_hand = deal(deck)
    dealer_hand = deal(deck)

    bet = 0
    while True:
        try:
            bet = int(input('Enter your bet: '))
            if bet <= 0:
                print('Bet must be a positive integer.')
            elif bet > budget:
                print(f'You cannot bet more than your budget of {budget}.')
            else:
                break
        except ValueError:
            print('Invalid bet. Please enter an integer.')

    print(f'Player hand: {player_hand} with total {total(player_hand)}')
    print(f'Dealer hand: {dealer_hand[0]}')

    if total(player_hand) == 21:
        print('Blackjack! Player wins!')
        budget += 1.5 * bet
        print(f'Your budget is now {budget}')
        return
    elif total(dealer_hand) == 21:
        print('Blackjack! Dealer wins!')
        budget -= bet
        print(f'Your budget is now {budget}')
        return
    while total(player_hand) < 21:
        action = input('Do you want to [H]it or [S]tand? ').lower()
        if action == 'h':
            hit(player_hand)
            print(f'Player hand: {player_hand} with total {total(player_hand)}')
        elif action == 's':
            break

    while total(dealer_hand) < 17:
        clear(dealer_hand)

    player_score = total(player_hand)
    dealer_score = total(dealer_hand)

    print(f'Final scores: Player {player_score}, Dealer {dealer_score}')

    if player_score > 21:
        print('Player busts, Dealer wins!')
        budget -= bet
    elif dealer_score > 21:
        print('Dealer busts, Player wins!')
        budget += bet
    elif player_score > dealer_score:
        print('Player wins!')
        budget += bet
    elif dealer_score > player_score:
        print('Dealer wins!')
        budget -= bet
    else:
        print('It\'s a tie!')

    print(f'Your budget is now {budget}')

while True:
    game()
    if budget <= 0:
        print('You ran out of budget! Game over.')
        break
    play_again = input('Do you want to play again? (Yes/No) ').lower()
    if play_again != 'yes':
        break





