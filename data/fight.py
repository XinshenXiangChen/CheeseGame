'''
class Fight:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def attack(self, attacker, atacked):
        attacked.hp -= attacker.dmg #hngggg
'''

import pygame

pygame.init()


def fight(screen, event, enemy, player):

    enemy.hp -= player.attack
    player.bar -= ((player.full_bar * player.attack) / enemy.full_hp)
    # TODO: el player bar del principio se tiene que cambiar
    # TODO: uhmm esto hay que cambiarlo, no tedira que ser todo player

    if enemy.hp <= 0:
        winner = 'player'
        enemy.hp = enemy.full_hp

        player.reset()
        return winner










