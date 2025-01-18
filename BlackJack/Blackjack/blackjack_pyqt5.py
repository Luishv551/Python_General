import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt

class BlackjackGame(QWidget):
    def __init__(self):
        super().__init__()
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        self.budget = 100
        self.game_over = False
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Blackjack')
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()

        self.budget_label = QLabel(f'Orçamento: {self.budget}')
        layout.addWidget(self.budget_label)

        bet_layout = QHBoxLayout()
        self.bet_input = QLineEdit()
        bet_layout.addWidget(QLabel('Aposta:'))
        bet_layout.addWidget(self.bet_input)
        self.bet_button = QPushButton('Apostar')
        self.bet_button.clicked.connect(self.place_bet)
        bet_layout.addWidget(self.bet_button)
        layout.addLayout(bet_layout)

        self.player_hand_label = QLabel('Mão do jogador:')
        layout.addWidget(self.player_hand_label)
        self.player_total_label = QLabel('Total do jogador:')
        layout.addWidget(self.player_total_label)

        self.dealer_hand_label = QLabel('Mão do dealer:')
        layout.addWidget(self.dealer_hand_label)
        self.dealer_total_label = QLabel('Total do dealer:')
        layout.addWidget(self.dealer_total_label)

        button_layout = QHBoxLayout()
        self.hit_button = QPushButton('Hit')
        self.hit_button.clicked.connect(self.hit)
        button_layout.addWidget(self.hit_button)
        self.stand_button = QPushButton('Stand')
        self.stand_button.clicked.connect(self.stand)
        button_layout.addWidget(self.stand_button)
        layout.addLayout(button_layout)

        self.message_label = QLabel('')
        layout.addWidget(self.message_label)

        self.new_game_button = QPushButton('Novo Jogo')
        self.new_game_button.clicked.connect(self.new_game)
        layout.addWidget(self.new_game_button)

        self.setLayout(layout)

        self.reset_game()

    def reset_game(self):
        if len(self.deck) < 20:
            self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        random.shuffle(self.deck)
        self.player_hand = []
        self.dealer_hand = []
        self.bet = 0
        self.game_over = False
        self.update_labels()
        self.bet_button.setEnabled(True)
        self.hit_button.setEnabled(False)
        self.stand_button.setEnabled(False)
        self.bet_input.setEnabled(True)
        self.message_label.setText('')

    def update_labels(self):
        self.budget_label.setText(f'Orçamento: {self.budget}')
        self.player_hand_label.setText(f'Mão do jogador: {self.player_hand}')
        self.player_total_label.setText(f'Total do jogador: {self.calculate_total(self.player_hand)}')
        if self.dealer_hand:
            if self.game_over:
                self.dealer_hand_label.setText(f'Mão do dealer: {self.dealer_hand}')
                self.dealer_total_label.setText(f'Total do dealer: {self.calculate_total(self.dealer_hand)}')
            else:
                visible_card = self.dealer_hand[0]
                self.dealer_hand_label.setText(f'Mão do dealer: [{visible_card}, *]')
                self.dealer_total_label.setText(f'Total visível do dealer: {visible_card}')
        else:
            self.dealer_hand_label.setText('Mão do dealer:')
            self.dealer_total_label.setText('Total do dealer:')

    def calculate_total(self, hand):
        total = sum(hand)
        aces = hand.count(11)
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def place_bet(self):
        try:
            bet = int(self.bet_input.text())
            if 0 < bet <= self.budget:
                self.bet = bet
                self.deal_initial_hands()
                self.bet_button.setEnabled(False)
                self.bet_input.setEnabled(False)
                if self.calculate_total(self.player_hand) == 21:
                    self.blackjack()
                else:
                    self.hit_button.setEnabled(True)
                    self.stand_button.setEnabled(True)
            else:
                self.message_label.setText('Aposta inválida!')
        except ValueError:
            self.message_label.setText('Por favor, insira um número válido!')

    def deal_initial_hands(self):
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]
        self.update_labels()

    def deal_card(self):
        return self.deck.pop()

    def hit(self):
        self.player_hand.append(self.deal_card())
        self.update_labels()
        if self.calculate_total(self.player_hand) > 21:
            self.bust()
        elif self.calculate_total(self.player_hand) == 21:
            self.stand()

    def stand(self):
        self.hit_button.setEnabled(False)
        self.stand_button.setEnabled(False)
        self.dealer_play()
        self.end_game()

    def dealer_play(self):
        while self.calculate_total(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deal_card())

    def blackjack(self):
        self.game_over = True
        self.update_labels()
        if len(self.dealer_hand) == 2 and self.calculate_total(self.dealer_hand) == 21:
            self.message_label.setText('Empate! Ambos têm Blackjack.')
        else:
            self.budget += int(self.bet * 1.5)
            self.message_label.setText('Blackjack! Você ganhou 1.5x a aposta!')
        self.end_round()

    def bust(self):
        self.game_over = True
        self.budget -= self.bet
        self.update_labels()
        self.message_label.setText('Você estourou! Dealer ganha!')
        self.end_round()

    def end_game(self):
        self.game_over = True
        self.update_labels()
        player_total = self.calculate_total(self.player_hand)
        dealer_total = self.calculate_total(self.dealer_hand)

        if dealer_total > 21:
            self.budget += self.bet
            self.message_label.setText('Dealer estourou! Você ganhou!')
        elif player_total > dealer_total:
            self.budget += self.bet
            self.message_label.setText('Você ganhou!')
        elif dealer_total > player_total:
            self.budget -= self.bet
            self.message_label.setText('Dealer ganhou!')
        else:
            self.message_label.setText('Empate!')
        
        self.end_round()

    def end_round(self):
        self.update_labels()
        self.bet_button.setEnabled(False)
        self.hit_button.setEnabled(False)
        self.stand_button.setEnabled(False)
        if self.budget <= 0:
            self.message_label.setText('Você ficou sem dinheiro! Fim de jogo.')
            self.new_game_button.setEnabled(False)
        else:
            self.new_game_button.setEnabled(True)

    def new_game(self):
        self.reset_game()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = BlackjackGame()
    game.show()
    sys.exit(app.exec_())