from screens import *
from main import gta_gamehorses

'''
Instancia o programa, chama o menu e os fluxos de execuções das telas.
'''


def control_start():
    game = menu()
    if game == 1:
        comeback = gta_gamehorses(True)
        if comeback == 0:
            pass
        elif comeback == 1:
            control_start()
    elif game == 2:
        comeback = gta_gamehorses(False)
        if comeback == 0:
            pass
        elif comeback == 1:
            control_start()


if __name__ == '__main__':
    control_start()
