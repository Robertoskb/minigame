from random import choice, choices
from Game.utils.items import collectibles
from Game.utils.convert_items import convert_items

collectibles = convert_items(collectibles)


class LootBox:

    def __init__(self, name, weights, price):
        self.name = name
        self.weights = weights
        self.price = price

    def give_way(self, coins):
        key, given = None, None
        msg = "Moedas insuficientes!"

        if coins >= self.price:
            key, given, coins = self._draw(coins)
            msg = f"Você ganhou um item {given.rarity}: {given}"

        print(msg)

        return key, given, coins

    def _draw(self, coins):
        key = choices(list(collectibles.keys()), self.weights)[0]
        given = choice(collectibles[key].items)
        coins -= self.price

        return key, given, coins


class CommonBox(LootBox):

    def __init__(self):
        LootBox.__init__(self, 'Caixa Comum', [90, 5, 4, 1], 150)


class RareBox(LootBox):

    def __init__(self):
        LootBox.__init__(self, 'Caixa Rara', [10, 80, 8, 2], 300)


class EpicBox(LootBox):

    def __init__(self):
        LootBox.__init__(self, 'Caixa Épica', [5, 15, 75, 5], 500)


class LegendaryBox(LootBox):

    def __init__(self):
        LootBox.__init__(self, 'Caixa Lendária', [2, 8, 40, 50], 1000)
