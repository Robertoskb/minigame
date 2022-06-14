from random import choice, choices
from items import collectibles
from convert_items import convert_items

collectibles = convert_items(collectibles)


class LootBox:

    def __init__(self, weights, price=0):
        self.weights = weights
        self.price = price

    def give_way(self, coins):
        given = None
        msg = "Moedas insuficientes!"

        if coins >= self.price:
            given = choice(collectibles[choices(list(collectibles.keys()), self.weights)[0]].items)
            msg = f"Você ganhou um item {given.rarity}!"

        print(msg)

        return given


class CommonBox(LootBox):

    def __init__(self):
        LootBox.__init__(self, [90, 5, 4, 1])


class RareBox(LootBox):

    def __init__(self):
        LootBox.__init__(self, [10, 80, 8, 2])


class EpicBox(LootBox):

    def __init__(self):
        LootBox.__init__(self, [5, 15, 75, 5])


class LegendaryBox(LootBox):

    def __init__(self):
        LootBox.__init__(self, [2, 8, 40, 50])


print(EpicBox().give_way(0))
