from abstract_pokmeon import AsbtractPokemon
from abc import ABC, abstractmethod


class Attacker(AsbtractPokemon):

    def __init__(self):
        super.__init__(stat_max=None, stat_current=None, level=0, name=None, type_pk="Attacker")

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.speed_current + self.attack_current) / 200
