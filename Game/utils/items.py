from Game.utils.json_manager import JsonManager
from os.path import relpath, dirname, join

collectibles = JsonManager(join(dirname(relpath(__file__)), 'data/items.json')).read_json()


class Items:

    def __init__(self, key, items, color):
        self.key = key
        self.items = items
        self.color = color

    def __iter__(self):
        for item in self.items:
            yield item

    def __getitem__(self, item):
        return self.items[item]

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f'{self.key}([{", ".join(map(str, self))}])'

    def append(self, __object):
        self.items.append(__object)

    @property
    def found(self):
        return f'{self.color}{self.key} {len(self.items)}/{len(collectibles[self.key])}\033[0;0m'


class CommonItems(Items):

    def __init__(self, items):
        Items.__init__(self, 'Comuns', list(map(CommonItem, items)), '\033[1;37m')


class RareItems(Items):

    def __init__(self, items):
        Items.__init__(self, 'Raros', list(map(RareItem, items)), '\033[1;36m')


class EpicItems(Items):

    def __init__(self, items):
        Items.__init__(self, 'Épicos', list(map(EpicItem, items)), '\033[1;34m')


class LegendaryItems(Items):

    def __init__(self, items):
        Items.__init__(self, 'Lendários', list(map(LegendaryItem, items)), '\033[1;33m')


class Item:

    def __init__(self, item, rarity, color):
        self.item = item
        self.rarity = f'{color}{rarity}\033[0;0m'

    def __str__(self):
        return str(self.item)

    def __repr__(self):
        return f'Item({self.item}, {self.rarity})'

    def __eq__(self, other):
        return self.item == other


class CommonItem(Item):

    def __init__(self, item):
        Item.__init__(self, item, 'Comum', '\033[1;37m')


class RareItem(Item):

    def __init__(self, item):
        Item.__init__(self, item, 'Raro', '\033[1;36m')


class EpicItem(Item):

    def __init__(self, item):
        Item.__init__(self, item, 'Épico', '\033[1;34m')


class LegendaryItem(Item):

    def __init__(self, item):
        Item.__init__(self, item, 'Lendário', '\033[1;33m')
