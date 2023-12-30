from collections import Counter
import copy
from dataclasses import dataclass


file = open('day7/input.txt', 'r')
lines = file.read().splitlines()

CARD_MAP = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 12,
    "K": 13,
    "A": 14, 
}

VALUE_MAP = {
    1 :"J",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10 :"T",
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
    new_cards: list[int]
    bet: int

    def __str__(self) -> str:
        old = "".join([VALUE_MAP[x] for x in self.cards])
        new = "".join([VALUE_MAP[x] for x in self.new_cards])
        return f'OLD:{old} | NEW:{new} - {self.bet}'

    def get_type(self, cards) -> str:
        counter = Counter(cards)
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

    def generate_best_cards(self):
        counter = Counter(self.cards)
        if self.bet == 756:
            print('hey')
        if counter[1] > 0:
            # we have jacks
            if counter[1] == 5:
                high_value = 14
            else:
                common = sorted(counter.most_common(), key=lambda x: (x[1], x[0]), reverse=True)
                high_value = common[0][0] if common[0][0] != 1 else common[1][0]

            for card in self.cards:
                if card == 1:
                    self.new_cards.append(high_value)
                else:
                    self.new_cards.append(card)
        else:
            self.new_cards = self.cards
    
    def score(self) -> list[int]:
        if self.new_cards:
            type_rank = HAND_MAP[self.get_type(self.new_cards)]
        else:
            type_rank = HAND_MAP[self.get_type(self.cards)]
        return [type_rank] + self.cards

hands: list[Hand] = []
for line in lines:
    line_str = line.split()
    cards = [CARD_MAP[x] for x in line_str[0].split()[0]]
    hand = Hand(cards, [], int(line_str[1]))
    # print(f'{hand} - {hand.get_type()} - {hand.score()}')
    hand.generate_best_cards()
    # print(f'{hand} - {hand.get_type()} - {hand.score()}')
    hands.append(hand)

hands.sort(key=lambda hand: (hand.score()[0], hand.score()[1], hand.score()[2], hand.score()[3], hand.score()[4], hand.score()[5]))
total_bet = 0
for index, hand in enumerate(hands):
    print(f'{index + 1}: {hand.get_type(hand.new_cards)} - {hand.score()} - {hand}')
    total_bet += (index + 1) * hand.bet
print(total_bet)