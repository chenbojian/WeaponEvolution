from .player import Player


class DuelCenter:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def start_duel(self):
        while self.player1.is_alive() and self.player2.is_alive():
            self.player1.attack(self.player2)
            self.player2.attack(self.player1)