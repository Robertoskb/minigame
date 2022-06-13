from Game.utils.items import CommonItems, RareItems, EpicItems, LegendaryItems, collectibles
from Game.utils.json_manager import JsonManager
from Game.utils.menu import menu, clear


def convert_items(data):
    def convert(k, v):
        return {'Comuns': CommonItems, 'Raros': RareItems,
                'Épicos': EpicItems, 'Lendários': LegendaryItems}[k](v)

    items = {k: convert(k, v) for k, v in data.items()}

    return items


class MiniGames:

    def __init__(self, json_manager: JsonManager, name: str, data: dict):
        self.name = name
        self.coins = data['moedas']
        self.items = convert_items(data['itens'])
        self.json_manager = json_manager

    def run(self):
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
