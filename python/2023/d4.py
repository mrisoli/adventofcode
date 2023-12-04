import re
from utils import str_list

def parse_ticket(t):
    return set(re.findall(r'\d+', t))

def matches(it):
    return len(set.intersection(*it))

def score(g):
    game, tickets = g.split(':')
    game = int(re.search(r'\d+', game).group(0))
    return game,matches(map(parse_ticket, tickets.split('|')))

def generate():
    return dict(map(score, str_list(4)))
