import random

deck = []
waste = []
player_hand = []
IA_hand = []

# this function rule the distribution of cards to the players
def pick(hand):
    hand.append(deck.pop())
    if playable(hand):
        waste.append(hand.pop())


def playable(hand):
    playable_card = []
    for card in hand:
        IA_numb = card[0]
        IA_letter = card[1]
        waste_card = waste[-1]
        player_numb = waste_card[0]
        player_letter = waste_card[1]
        if IA_numb == player_numb or IA_letter == player_letter:
            playable_card.append(card)
    return playable_card


def IA_turn(hand):
    cards = playable(hand)
    if cards:
        random.shuffle(cards)
        waste.append(hand.pop(hand.index(cards[-1])))
        print(f"L'IA pose un {waste[-1]}")
    else:
        pick(hand)
        print("L'IA pioche")


def player_turn(hand):
    if playable(hand):
        print(f"Michel : {len(IA_hand)} cartes restantes")
        print(f"défausse : {waste[-1]}")
        print(f"main : {hand}")

        carte = str(input("Carte a jouer :"))
        waste.append(hand.pop(hand.index(carte)))
    else:
        pick(hand)
        print("Vous piochez")


def game():
    while player_hand or IA_hand:
        if len(player_hand) >= 1:
            player_turn(player_hand)
        elif len(player_hand) <= 1:
            print("Joueur Gagne")
            break
        elif len(IA_hand) >= 1:
            IA_turn(IA_hand)
        elif len(IA_hand) <= 1:
            print("IA Gagne")
            break

# this function rule the distribution of cards to the players
def start():
    random.shuffle(deck)
    for i in range(0, 2):
        player_hand.append(deck.pop())
        IA_hand.append(deck.pop())
    waste.append(deck.pop())
    game()


start()
