from weapon_evolution.player import Player
from weapon_evolution.duel_center import DuelCenter


def test_player_can_attack_another_player():
    zhang = Player(name='zhang', life_value=100, attack_value=3)
    li = Player(name='li', life_value=100, attack_value=1)
    zhang.attack(li)
    assert li.life_value == 97


def test_duel_center_can_arrange_duel():
    zhang = Player(name='zhang', life_value=100, attack_value=3)
    li = Player(name='li', life_value=100, attack_value=1)
    duel_center = DuelCenter(player1=zhang, player2=li)
    duel_center.start_duel()
    assert zhang.is_alive() is True
    assert li.is_alive() is False


