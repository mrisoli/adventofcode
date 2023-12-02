from utils import str_list

MAX_COLORS = { 'blue': 14, 'green': 13, 'red': 12 }
def parse_game(game):
    for d in game.strip(' ').split(', '):
        n, c = d.split(' ')
        if int(n) > MAX_COLORS[c]:
            return False
    return True

def game_possible(data):
    return all(map(parse_game, data.split(';')))

def get_data(g):
    return g.split(':')

def games(l):
    return sum([int(gid.split(' ')[1]) for gid, data in map(get_data, l) if game_possible(data)])

print(games(str_list(2)))
