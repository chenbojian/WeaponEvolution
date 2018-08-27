from weapon_evolution.player import Player


def test_player_can_attack_another_player():
    zhang = Player(name='zhang', life_value=100, attack_value=3)
    li = Player(name='li', life_value=100, attack_value=1)
    zhang.attack(li)
    assert li.life_value == 97
