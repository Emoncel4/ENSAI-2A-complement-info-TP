from abstract_pokmeon import AsbtractPokemon
from abc import ABC, abstractmethod


class AllRounder(AsbtractPokemon):

    def __init__(self):
        super.__init__(stat_max=None, stat_current=None, level=0, name=None, type_pk="All Rounder")

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.sp_atk_current + self.sp_def_current) / 200
