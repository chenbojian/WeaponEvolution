class Player:
    def __init__(self, name, life_value, attack_value):
        self.name = name
        self.life_value = life_value
        self.attack_value = attack_value

    def attack(self, enemy_player: 'Player'):
        enemy_player.life_value = enemy_player.life_value - self.attack_value

    def is_alive(self):
        return self.life_value > 0


class DuelCenter:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2

    def start_duel(self):
        while self.player1.is_alive() and self.player2.is_alive():
            self.player1.attack(self.player2)
            self.player2.attack(self.player1)
