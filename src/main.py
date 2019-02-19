from pyramid import Env

config = {
    'floor': 7,
    'players': ['random', 'first_move'],
    'nb_card': 5,
    'nb_round': 2
}

env = Env(config)

env.reset()

