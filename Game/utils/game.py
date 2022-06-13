from Game.utils.json_manager import JsonManager
from Game.utils.menu import menu, clear
from Game.utils.minigames import MiniGames
from os.path import dirname, relpath, join


def create_data(filepath):
    manager = JsonManager(filepath)

    if not manager.read_json():
        manager.create_json()

    return manager.read_json()


class Game:

    def __init__(self):
        self.root = dirname(relpath(__file__)) + '/'
        self.data_path = join(self.root, 'data/data.json')
        self.data = create_data(self.data_path)
        self.json_manager = JsonManager(self.data_path)

    def run(self):
        while True:
            functions = {'novo jogo': self.create_profile,
                         'carregar jogo': self.profiles,
                         'excluir jogo': self.delete_profile,
                         'sair': exit}

            functions[menu(functions)]()

    def profiles(self):
        if not self.data:
            return print("nenhum jogo salvo")
        clear()

        profile = menu(self.data, True)

        if profile:
            MiniGames(self.json_manager, profile, self.data[profile]).run()

    def create_profile(self):
        name = self._get_name()

        self.data[name] = {"moedas": 0, "itens": {"Comuns": [], "Raros": [], "Épicos": [], "Lendários": []}}
        self.json_manager.update_json(self.data)
        MiniGames(self.json_manager, name, self.data[name]).run()

    def _get_name(self):
        name = input('nome: ').strip()
        while name in self.data or name == '':
            clear()
            print('nome', 'já existe!' if name in self.data else 'inválido!')
            name = input('nome: ').strip()

        clear()
        return name

    def delete_profile(self):
        profile = menu(self.data, True)
        if profile:
            self.data.pop(profile)
            JsonManager(self.data_path).update_json(self.data)
