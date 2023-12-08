from functools import cmp_to_key

card_ranks = {card: rank for rank, card in enumerate("J23456789TQKA")}


def run():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    plays = [(line[:5], int(line[6:].strip())) for line in lines]
    print(plays[:5])

    plays.sort(key=cmp_to_key(comparator))
    print(plays[:5])

    print(sum(play[1] * (idx+1) for idx, play in enumerate(plays)))


def comparator(A, B):
    A, B = A[0], B[0]
    rankA, rankB = rank(A), rank(B)

    if rankA != rankB:
        return rankA - rankB
    
    for i in range(5):
        cardA, cardB = card_ranks[A[i]], card_ranks[B[i]]
        if cardA != cardB:
            return cardA - cardB
        
    return 0


def rank(hand):
    if len(hand) != 5:
        return -1
    
        
    s = set(hand)
    

    if len(s) == 1:
        return 7
    elif hand.count("J"):
        counts = {}
        for char in list(s):
            if char != "J":
                count = hand.count(char)
                if count not in counts:
                    counts[count] = []
                counts[count].append(char)
        most = max(counts.keys())
        return rank(hand.replace("J", counts[most][0]))
    elif len(s) == 2:
        count = hand.count(s.pop())
        if count == 1 or count == 4:
            return 6
        return 5
    elif len(s) == 3:
        if any(hand.count(char) == 3 for char in list(s)):
            return 4
        return 3
    elif len(s) == 4:
        return 2
    
    return 1



class Hand:

    def __init__(self, hand: str, bet: int):
        self.hand = hand
        self.bet = bet

    

if __name__ == "__main__":
    run()