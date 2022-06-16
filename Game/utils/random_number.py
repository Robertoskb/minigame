from random import randint
from Game.utils.menu import menu, clear


class RandomNumber:

    def __init__(self, name: str, award: int, price: int, end: int, attempts: int):
        self.name = name
        self.award = award
        self.price = price
        self.end = end
        self.attempts = attempts
        self.clues = None

    def run(self, coins):
        if coins >= self.price:
            coins += self.play()

        else:
            print("Moedas insuficientes")

        return coins

    def play(self):
        self.clues, award = self._activate_clues()

        number, attempts = randint(1, self.end), self.attempts
        print(f'Tente adivinhar um número aleatório entre 1 e {self.end}')
        while attempts:
            print(f'Tentativas restantes: {attempts}')
            print(f'Prêmio: {award}')

            if self._check_response(input('Jogada: '), number):
                print(f'Número correto! +{award} moedas')
                return award

            award -= round(award * 0.1) if award > self.award * .5 else 0
            attempts -= 1

        clear()
        print(f'Você perdeu! Número correto: {number}')

        return -self.price

    def _check_response(self, response, number):
        clear()
        try:
            response = int(response)
            if response == number:
                return True

            if self.clues:
                if response > number:
                    print('digite um número menor!')

                else:
                    print('digite um número maior')

        except ValueError:
            print('digite um número!')

    def _activate_clues(self):
        options = {f'Com dicas: até {self.award} moedas': True,
                   f'Sem dicas: até {self.award * 10} moedas': False}

        clues = options[menu(options=options)]
        award = self.award

        if not clues:
            award *= 10

        return clues, award

    def __str__(self):
        return self.name


class Random10(RandomNumber):

    def __init__(self):
        RandomNumber.__init__(self, 'Random10', 10, 0, 10, 5)


class Random100(RandomNumber):

    def __init__(self):
        RandomNumber.__init__(self, 'Random100', 100, 20, 100, 10)


class Random1000(RandomNumber):

    def __init__(self):
        RandomNumber.__init__(self, 'Random1000', 300, 100, 1000, 15)


class Random10000(RandomNumber):

    def __init__(self):
        RandomNumber.__init__(self, 'Random10000', 1000, 300, 10000, 20)
