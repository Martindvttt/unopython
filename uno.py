import random
import secrets


def create_deck():
    deck = []
    j = 0
    for i in range(0, 10):
        itoa = str(i)
        deck.append(itoa + "R")
        deck.append(itoa + "G")
        deck.append(itoa + "B")
        deck.append(itoa + "Y")
        if i >= 1:
            deck.append(itoa + "R")
            deck.append(itoa + "G")
            deck.append(itoa + "B")
            deck.append(itoa + "Y")
    for i in range(0, 3):
        deck.append("+2R")
        deck.append("+2G")
        deck.append("+2B")
        deck.append("+2Y")
    for i in range(0, 4):
        deck.append("+4")
    return deck


deck = create_deck()
tab_waste = []
hand_player = []
hand_ai = []

# ----Display---- #


def display(index):
    input_str = {
        1: "La carte piochée à été posée",
        2: f"Carte posée : {tab_waste[-1]}",
        3: "Vous piochez",
        4: "L'IA pioche",
        5: "Joueur gagne",
        6: "IA gagne",
    }
    output = 0
    print("|********************** UNO **********************|")
    print()
    print('Michel'.center(50))
    print(f"{len(hand_ai)} cartes restantes".center(50))
    print()
    print()
    print()
    print(f"Fosse : {tab_waste[-1]}".center(50))
    print()
    print()
    print()
    print(f"{hand_player}".center(50))
    if index < 7:
        print(input_str[index].center(50))
    elif index == 7:
        output = str(input('Carte a jouer :'))
    print()
    print()
    print("|********************** *** **********************|")
    return output


def pick(hand, count):
    for i in range(0, count):
        hand.append(deck.pop())
    if hand == hand_ai:
        display(4)
    elif hand == hand_player:
        display(3)


def waste(hand, card):
    if card[0] == "+":
        if card[1] == "2":
            tab_waste.append(hand.pop(hand.index(card)))
            if hand == hand_player:
                pick(hand_ai, 2)
            elif hand == hand_ai:
                pick(hand_player, 2)
        if card[1] == "4":
            if hand == hand_player:
                pick(hand_ai, 4)
            elif hand == hand_ai:
                card.append(secrets.choice("R", "V", "B", "Y"))
                pick(hand_player, 4)
            tab_waste.append(hand.pop(hand.index(card)))
    else:
        tab_waste.append(hand.pop(hand.index(card)))


def check_card(hand):
    solutions = []
    to_compare = tab_waste[-1]
    for card in hand:
        if card[0] == "+":
            if card[1] == "2":
                number = card[1]
                letter = card[2]
            if card[1] == "4":
                solutions.append(card)
        else:
            number = card[0]
            letter = card[1]
        if to_compare[0] == "+":
            to_compare_number = to_compare[1]
            to_compare_letter = to_compare[2]
        else:
            to_compare_number = to_compare[0]
            to_compare_letter = to_compare[1]
        if card[0] == "+" or to_compare[0] == "+":
            if letter == to_compare_letter:
                solutions.append(card)
            elif number == to_compare_number:
                solutions.append(card)
        else:
            if number == to_compare_number or letter == to_compare_letter:
                solutions.append(card)
    return solutions


def tour_ai(hand):
    cards = check_card(hand)
    if cards:
        random.shuffle(cards)
        waste(hand, cards[-1])
        display(2)
    else:
        pick(hand, 1)
        if check_card(hand):
            tab_waste.append(hand.pop())
            display(1)


def tour_player(hand):
    if check_card(hand):
        card = display(7)
        waste(hand, card)
    else:
        pick(hand, 1)


def launch_game():
    lap = 0
    while hand_player or hand_ai:
        if len(hand_player) >= 1 and lap == 0:
            tour_player(hand_player)
            lap = 1
        elif len(hand_player) < 1:
            display(5)
            break
        elif len(hand_ai) >= 1 and lap == 1:
            tour_ai(hand_ai)
            lap = 0
        elif len(hand_ai) < 1:
            display(6)
            break


def start():
    random.shuffle(deck)
    for i in range(0, 7):
        hand_player.append(deck.pop())
        hand_ai.append(deck.pop())
    tab_waste.append(deck.pop())
    launch_game()


start()