from Game.utils.items import CommonItems, RareItems, EpicItems, LegendaryItems


def convert_items(data):
    def convert(k, v):
        return {'Comuns': CommonItems, 'Raros': RareItems,
                'Épicos': EpicItems, 'Lendários': LegendaryItems}[k](v)

    items = {k: convert(k, v) for k, v in data.items()}

    return items
