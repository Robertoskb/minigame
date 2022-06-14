from Game.utils.lootbox import CommonBox, RareBox, EpicBox, LegendaryBox
from Game.utils.menu import menu


class Store:

    def __init__(self, coins):
        self.coins = coins

    def purchases(self):
        options = self._get_options()

        while True:
            loot_box = menu(options=options, cancel=True, head=f'Moedas: {self.coins}')

            if loot_box:
                key, given, self.coins = options[loot_box].give_way(self.coins)

                yield key, given, self.coins

            else:
                return

    @staticmethod
    def _get_options():
        boxs = (CommonBox(), RareBox(), EpicBox(), LegendaryBox())

        return {f'{box.name} - ({box.price} moedas)': box for box in boxs}
