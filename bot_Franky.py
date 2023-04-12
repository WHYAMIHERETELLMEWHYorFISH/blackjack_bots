import sys
from cards import Card
ranks = ["", "A", "2", "3", "4", "5", "6",
         "7", "8", "9", "10", "J", "Q", "K"]
suits = ["H", "C", "S", "D"]


def blackjack_score(hand):
    score = 0
    ace_count = 0
    for card in hand:
        if card.rank == 1:
            score += 11
            ace_count += 1
        elif card.rank >= 10:
            score += 10
        else:
            score += card.rank
    for i in range(ace_count):
        if score > 21:
            score-=10
    return score

# Gets the input from the command line and converts to a list of Card objects.
hand = [Card(suits.index(card_str[-1]),
        ranks.index(card_str[:-1])) for card_str in sys.argv[1:]]
print(blackjack_score(hand))

def get_decision(hit, split, stand, doubledown):
    if card1 = card2:
        return split
    if score = 21:
        return doubledown
    if score < 12:
        return hit
    if score > 12 and <= 21:
        then stand

