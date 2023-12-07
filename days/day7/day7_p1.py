input_file = "../../puzzle.input/day7.txt"

ans = 0

cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

with open(input_file, "r") as F:
    lines = F.read().split("\n")

cards_in_hands = {}

types = {1: [], 2:[], 3: [], 4:[], 5: [], 6: []}

for i in range(len(lines)):
    cards_in_hands[i] = {}
    hand = lines[i].split()[0]
    bid = lines[i].split()[1]



    for card in hand:
        if card not in cards_in_hands[i]:
            cards_in_hands[i][card] = 1
        else:
            cards_in_hands[i][card] += 1

for hand in cards_in_hands:
    print(hand)
    for card in cards_in_hands[hand]:
        __found = False
        num = cards_in_hands[hand][card]
        if num == 5:
            types[1].append(hand)
        elif num == 4:
            types[2].append(hand)
        elif num == 3:
            types[3].append(hand)
        elif num == 2:
            if not __found:
                for _card in cards_in_hands[hand]:
                    if _card != card:
                        if cards_in_hands[hand][_card] == 2:
                            types[4].append(hand)
                            __found = True
                            continue
                if not __found:
                    types[5].append(hand)

        elif len(cards_in_hands[hand]) == 5:
            types[6].append(hand)
# github teszt
print(types)
