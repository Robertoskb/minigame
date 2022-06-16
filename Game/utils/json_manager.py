from os.path import isfile
from json import dump, load


class JsonManager:

    def __init__(self, filepath):
        self.filepath = filepath

    def create_json(self):
        data = {}

        with open(self.filepath, 'w', encoding='utf-8') as f:
            dump(data, f, indent=2, separators=(',', ': '))

    def read_json(self):
        if isfile(self.filepath):
            with open(self.filepath, encoding='utf-8') as f:
                data = load(f)
            return data

    def update_json(self, data):
        with open(self.filepath, 'w', encoding='utf-8') as f:
            dump(data, f, indent=2, separators=(',', ': '))
