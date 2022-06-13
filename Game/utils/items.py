from Game.utils.json_manager import JsonManager
from os.path import relpath, dirname, join

collectibles = JsonManager(join(dirname(relpath(__file__)), 'data/items.json')).read_json()


class Item:

    def __init__(self, item, rarity, color):
        self.item = item
        self.rarity = f'{color}{rarity}\033[0;0m'

    def __str__(self):
        return str(self.item)

    def __repr__(self):
        return f'Item({self.item}, {self.rarity})'


class Items:

    def __init__(self, key, items, color):
        self.key = key
        self.items = items
        self.color = color

    def __iter__(self):
        for item in self.items:
            yield item

    def __str__(self):
        return f'{self.color}{self.key} {len(self.items)}/{len(collectibles[self.key])}\033[0;0m'

    def __len__(self):
        return len(self.items)


class CommonItems(Items):

    def __init__(self, items):
        Items.__init__(self, 'Comuns', list(map(lambda i: Item(i, 'comum', '\033[1;37m'), items)), '\033[1;37m')


class RareItems(Items):

    def __init__(self, items):
        Items.__init__(self, 'Raros', list(map(lambda i: Item(i, 'raro', '\033[1;36m'), items)), '\033[1;36m')


class EpicItems(Items):

    def __init__(self, items):
        Items.__init__(self, 'Épicos', list(map(lambda i: Item(i, 'épico', '\033[1;34m'), items)), '\033[1;34m')


class LegendaryItems(Items):

    def __init__(self, items):
        Items.__init__(self, 'Lendários', list(map(lambda i: Item(i, 'lendário', '\033[1;33m'), items)), '\033[1;33m')
