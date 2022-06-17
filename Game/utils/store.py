from Game.utils.lootbox import CommonBox, RareBox, EpicBox, LegendaryBox
from Game.utils.random_number import Random10, Random100, Random1000, Random10000
from Game.utils.menu import menu


def space(values, value):
    return " " * (len(max(map(str, values), key=lambda b: len(b))) + 1 - len(str(value)))


class Store:

    def __init__(self, coins):
        self.coins = coins

    def box_purchases(self):
        options = self._get_box_options()

        while True:
            loot_box = menu(options=options, cancel=True, head=f'Moedas: {self.coins}')

            if loot_box:
                key, given, self.coins = options[loot_box].give_way(self.coins)

                yield key, given, self.coins

            else:
                return

    def match_purchases(self):
        options = self._get_match_options()

        while True:
            random_number = menu(options=options, cancel=True, head=f'Moedas: {self.coins}')

            if random_number:
                self.coins = options[random_number].run(self.coins)

                yield self.coins

            else:
                return

    @staticmethod
    def _get_box_options():
        boxs = (CommonBox(), RareBox(), EpicBox(), LegendaryBox())

        return {f'{box.name}{space(boxs, box)}({box.price} moedas)': box for box in boxs}

    @staticmethod
    def _get_match_options():
        matches = (Random10(), Random100(), Random1000(), Random10000())

        return {f'{match.name}{space(matches, match)}Preço/Prêmio: {match.price}/{match.award} moedas': match for match in matches}
