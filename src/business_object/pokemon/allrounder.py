from abstract_pokmeon import AsbtractPokemon
from abc import ABC, abstractmethod


class AllRounder(AsbtractPokemon):

    def __init__(self):
        super.__init__(type_pk="All Rounder")
