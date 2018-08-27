class DuelCenter:
    def __init__(self, players):
        if len(players) != 2:
            raise ValueError()

        self._current_player, self._enemy_player = players

    def _swap_player(self):
        self._current_player, self._enemy_player = (self._enemy_player, self._current_player)

    def _round(self):
        self._current_player.attack(self._enemy_player)
        self._swap_player()

    def start_duel(self):
        while self._current_player.is_alive() and self._enemy_player.is_alive():
            self._round()
