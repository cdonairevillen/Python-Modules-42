#!/usr/bin/env python3

from typing import Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    """
    Class that inherit from Card, Combatable and Magical and reinterpretate
    all his functions.

    Methods:
        - get_card_info(): Reconstructs and returns a dictionary with all the
        card entries and adds the creature info to it.
        - play(): Creates a dictionary with te changes generated to the
        game_state by playing the selected card.
        - attack(): Simulates a atack from the selected card to the card
        marques as a target
        - defend(): Simulates a damage reception and a block effect.
        - get_combat_stats(): returns a dictionary of all the melee combat
        information.
        - cast_spell(): cast a specific spell send by the player. It returns
        a summary to actualize the game_state.
        - channel_mana(): adds x mana to the gamestate. It returns a dictionary
        with the information to actualize the game_state.
        - get_magic_stats(): returns a dictionary with all the information of
        the magic split of the card.
    """

    def __init__(self, name, cost, rarity, damage, health, block):
        super().__init__(name, cost, rarity)
        if damage >= 0 and health >= 0:
            self.damage = damage
            self.health = health
            self.block = block
            self.type = "Elite Card"
            self.mana = 5
        else:
            raise ValueError

    def play(self, game_state: Dict) -> Dict:

        played_card = {}

        if super().is_playable(game_state["mana"]) is True:
            game_state["mana"] -= self.cost
            played_card["name"] = self.name
            played_card["mana_used"] = self.cost
            played_card["effect"] = "Creature summoned to battlefield"
            return played_card
        else:
            return ("You can not play this card")

    def get_card_info(self):
        main_info = super().get_card_info()
        main_info["type"] = self.type
        main_info["attack"] = self.damage
        main_info["health"] = self.health
        main_info["block_capability"] = self.block
        return main_info

    def attack(self, target: Card) -> Dict:

        if target.type in ["Creature", "Elite Card"]:
            self.health -= target.attack
            target.health -= self.damage

            summary = {
                "attacker": self.name,
                "target": target.name,
                "damage": self.damage,
                "combat_type": "melee"
            }
            return summary
        else:
            return {"combat_resolved": False}

    def defend(self, incoming_damage: int) -> Dict:

        self.health -= incoming_damage - self.block
        summary = {
            "defender": self.name,
            "damage_taken": incoming_damage - self.block,
            "damage_blocked": self.block,
        }
        if self.health > 0:
            summary["still_alive"] = True
        else:
            summary["still_alive"] = False
        return summary

    def get_combat_stats(self) -> Dict:

        summary = {
            "name": self.name,
            "combat_type": "melee",
            "attack": self.damage,
            "health": self.health,
            "block_capability": self.block
        }
        return summary

    def cast_spell(self, spell_name: str, targets: list) -> Dict:

        if spell_name == "Defile":
            mana_cost = 2
            self.mana -= mana_cost

        elif spell_name == "Ligthning bolt":
            mana_cost = 1
            self.mana -= mana_cost

        summary = {
            "caster": self.name,
            "spell": spell_name,
            "targers": targets,
            "mana_used": mana_cost
        }
        return summary

    def channel_mana(self, amount: int) -> Dict:
        self.mana += amount

        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> Dict:

        summary = {
            "name": self.name,
            "mana": self.mana,
            "agic_type": "arcane"
        }
        return summary
