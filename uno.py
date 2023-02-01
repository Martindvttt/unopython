import random


# to create our uno's deck we use this function to generate an integer, transform it in string and concatenate with a letter, which is the color
def create_deck():
    deck = []
    j = 0
    for i in range(0, 10):
        # we know that we could do better but we haven't found how to do it
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


def display(index, index_player, card, count):
    player = {1: "Joueur", 2: "Michel"}
    input_str = {
        1: f"La carte {card} à été piochée",
        2: f"{player[index_player]} pose un {card}",
        3: f"{player[index_player]} pioche {count} cartes",
        5: f"{player[index_player]} gagne",
    }
    output = 0
    print("|********************** UNO **********************|")
    print()
    print("Michel".center(50))
    print(f"{len(hand_ai)} cartes restantes".center(50))
    print()
    print()
    print()
    print(f"Défausse : {tab_waste[-1]}".center(50))
    print()
    print()
    print()
    print(f"{hand_player}".center(50))
    if index < 6:
        print(input_str[index].center(50))
    elif index == 6:
        output = str(input("Carte a jouer :"))
    print()
    print()
    print("|********************** *** **********************|")
    return output


# ----End Display---- #


# it's used to gives a card to a player when he can't play
def pick(hand, count):
    for i in range(0, count):
        hand.append(deck.pop())
    if hand == hand_ai:
        display(3, 2, any, count)
    elif hand == hand_player:
        display(3, 1, any, count)


# this function handles the waste, it check if the player has chosen a +2 or +4 and dislay the last card played
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
                i = hand.index("+4")
                hand[i] = hand[i] + card[2]
                pick(hand_ai, 4)
            elif hand == hand_ai:
                i = hand.index("+4")
                colors = ["R", "G", "B", "Y"]
                hand[i] = hand[i] + random.choice(colors)
                card = hand[i]
                pick(hand_player, 4)
            tab_waste.append(hand.pop(hand.index(card)))
    else:
        tab_waste.append(hand.pop(hand.index(card)))
        if hand == hand_player:
            display(2, 1, card, any)
        elif hand == hand_ai:
            display(2, 2, card, any)


# the function gives to players the card which he could play
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


# this rules IA's turn, it takes playable cards and chooses which one it will play randomly
def ai_turn(hand):
    cards = check_card(hand)
    if cards:
        random.shuffle(cards)
        waste(hand, cards[-1])
    else:
        pick(hand, 1)


def player_turn(hand):
    if check_card(hand):
        card = display(6, 1, any, any)
        waste(hand, card)
    else:
        pick(hand, 1)


# with this we choose who have to play and which end display we have to show on screen
def launch_game():
    lap = 0
    while hand_player or hand_ai:
        if len(hand_player) >= 1 and lap == 0:
            player_turn(hand_player)
            lap = 1
        elif len(hand_player) < 1:
            display(5, 1, any, any)
            break
        elif len(hand_ai) >= 1 and lap == 1:
            ai_turn(hand_ai)
            lap = 0
        elif len(hand_ai) < 1:
            display(5, 2, any, any)
            break


# this function rule the distribution of cards to the players
def start():
    random.shuffle(deck)
    for i in range(0, 7):
        hand_player.append(deck.pop())
        hand_ai.append(deck.pop())
    tab_waste.append(deck.pop())
    launch_game()


start()
