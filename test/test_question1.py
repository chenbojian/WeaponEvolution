from weapon_evolution import Player as Player


def test_player_have_life_value():
    player = Player(100)
    assert player.life_value == 100
