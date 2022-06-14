from os import system, name


def clear():
    system('cls') if name == 'nt' else system('clear')


def menu(options, cancel=False, head=''):
    while True:
        if head: print(head)
        if cancel: print('[0] - cancelar')

        for c, k in enumerate(options):
            print(f'[{c + 1}] - {k}')

        try:
            op = int(input('op: ')) - 1
            if op < 0: raise IndexError

            clear()
            return list(options.keys())[op]

        except IndexError:
            clear()
            if op == -1 and cancel: return
            print('opção inválida')

        except ValueError:
            clear()
            print('digite um número')
