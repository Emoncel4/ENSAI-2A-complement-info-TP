from abstract_pokmeon import AsbtractPokemon
from abc import ABC, abstractmethod


class Defender(AsbtractPokemon):

    def __init__(self):
        super.__init__(stat_max=None, stat_current=None, level=0, name=None, type_pk="Defender")

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.attack_current + self.defense_current) / 200
