class Player:
    def __init__(self, name, life_value, attack_value):
        self.name = name
        self.life_value = life_value
        self.attack_value = attack_value

    def attack(self, enemy_player: 'Player'):
        enemy_player.life_value = enemy_player.life_value - self.attack_value

    def is_alive(self):
        return self.life_value > 0