import sys

def card_value(s):
    return int(s[0]) if s[0] in '23456789' else 10

lines = sys.stdin.readlines()
cases = int(lines[0])
original_deck = ' '.join(lines[1:]).split()
for case in range(cases):
    deck = original_deck[case * 52 : (case+1) * 52]
    deck = list(reversed(deck))
    saved = deck[0:25]
    whats_left = deck[25:]
    y = 0
    for i in range(3):
        x = card_value(whats_left[0])
        y += x
        whats_left = whats_left[1 + (10-x):]
    result = saved + whats_left
    answer = result[len(result) - y]
    print('Case {}: {}'.format(case+1, answer))
