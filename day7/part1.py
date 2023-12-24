from collections import Counter
from dataclasses import dataclass


file = open('day7/input.txt', 'r')
lines = file.read().splitlines()

CARD_MAP = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14, 
}

VALUE_MAP = {
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10 :"T",
    11 :"J",
    12 :"Q",
    13 :"K",
    14 :"A", 
}

HAND_MAP = {
    '5OAK': 6,
    '40AK': 5,
    'FULL': 4,
    '3OAK': 3,
    'TWOP': 2,
    'ONEP': 1,
    'HIGH': 0,
}

@dataclass
class Hand:
    cards: list[int]
    bet: int

    def __str__(self) -> str:
        return f'{"".join([VALUE_MAP[x] for x in self.cards])} - {self.bet}'

    def get_type(self) -> str:
        counter = Counter(self.cards)
        if len(counter) == 1:
            return '5OAK'
        elif len(counter) == 5:
            return 'HIGH'
        elif len(counter) == 4:
            return 'ONEP'
        elif len(counter) == 3:
            if counter.most_common()[0][1] == 3:
                return '3OAK'
            return 'TWOP'
        elif len(counter) == 2:
            if counter.most_common()[0][1] == 4:
                return '40AK'
            return 'FULL'

        return 'wtf'
    
    def score(self) -> list[int]:
        type_rank = HAND_MAP[self.get_type()]
        return [type_rank] + self.cards

hands: list[Hand] = []
for line in lines:
    line_str = line.split()
    hand = Hand([CARD_MAP[x] for x in line_str[0].split()[0]], int(line_str[1]))
    print(f'{hand} - {hand.get_type()} - {hand.score()}')
    hands.append(hand)

hands.sort(key=lambda hand: (hand.score()[0], hand.score()[1], hand.score()[2], hand.score()[3], hand.score()[4], hand.score()[5]))
total_bet = 0
for index, hand in enumerate(hands):
    print(f'{hand.get_type()} - {hand.score()} - {hand}')
    total_bet += (index + 1) * hand.bet
print(total_bet)