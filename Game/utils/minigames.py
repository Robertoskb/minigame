from Game.utils.items import collectibles
from Game.utils.convert_items import convert_items
from Game.utils.json_manager import JsonManager
from Game.utils.menu import menu, clear


class MiniGames:

    def __init__(self, json_manager: JsonManager, name: str, data: dict):
        self.name = name
        self.coins = data['moedas']
        self.items = convert_items(data['itens'])
        self.json_manager = json_manager

    def menu(self):
        while True:
            options = {'coleção': self.collection, 'salvar jogo': self.save_game, 'sair': exit}
            options[menu(options, head=self.progress)]()

    def collection(self):
        for v in self.items.values():
            print(v)
            print(', '.join(v), '\n')

        input('Enter para voltar: ')
        clear()

    def save_game(self):
        data = self.json_manager.read_json()
        data[self.name] = {'moedas': self.coins, 'itens': {k: list(map(str, v)) for k, v in self.items.items()}}
        self.json_manager.update_json(data)

    @property
    def progress(self):
        def _sum(d): return sum((len(v) for v in d.values()))
        return f'{self.name} \nprogresso: {int((_sum(self.items) / _sum(collectibles)) * 100)}%'
