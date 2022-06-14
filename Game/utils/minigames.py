from Game.utils.items import collectibles
from Game.utils.convert_items import convert_items
from Game.utils.json_manager import JsonManager
from Game.utils.menu import menu, clear
from Game.utils.story import Store


class SaveGame:

    def __init__(self, auto_save):
        self.auto_save = auto_save

    @staticmethod
    def autosave(function):
        def save_game(self, *args, **kwargs):
            function(self, *args, **kwargs)
            if self.auto_save:
                self.save_game()

        return save_game


class MiniGames(SaveGame):

    def __init__(self, json_manager: JsonManager, name: str, data: dict):
        self.name = name
        self.coins = data['moedas']
        self.items = convert_items(data['itens'])
        self.json_manager = json_manager
        SaveGame.__init__(self, True)

    def menu(self):
        while True:
            options = {'coleção': self.collection, 'loja': self.store, 'sair': exit}

            options[menu(options, head=self.progress)]()

    def collection(self):
        for v in self.items.values():
            print(v.found)
            print(', '.join(map(str, v)), '\n')

        input('Enter para voltar: ')
        clear()

    @SaveGame.autosave
    def store(self):
        store = Store(self.coins)

        for rarity, given, coins in store.purchases():
            if rarity:
                if given in self.items[rarity]:
                    print('Item repetido!\n')

                else:
                    print()
                    self.items[rarity].append(given)

            self.coins = coins

    def save_game(self):
        data = self.json_manager.read_json()
        data[self.name] = {'moedas': self.coins, 'itens': {k: list(map(str, v)) for k, v in self.items.items()}}

        self.json_manager.update_json(data)

    @property
    def progress(self):
        def _sum(d): return sum((len(v) for v in d.values()))
        return f'{self.name} \nprogresso: {int((_sum(self.items) / _sum(collectibles)) * 100)}%'
