import random

pioche = [
    "9G", "9G", "8G", "8G", "7G", "7G", "6G", "6G", "5G", "5G", "4G", "4G",
    "3G", "3G", "2G", "2G", "1G", "1G", "0G", "9Y", "9Y", "8Y", "8Y", "7Y",
    "7Y", "6Y", "6Y", "5Y", "5Y", "4Y", "4Y", "3Y", "3Y", "2Y", "2Y", "1Y",
    "1Y", "0Y", "9R", "9R", "8R", "8R", "7R", "7R", "6R", "6R", "5R", "5R",
    "4R", "4R", "3R", "3R", "2R", "2R", "1R", "1R", "0R", "9B", "9B", "8B",
    "8B", "7B", "7B", "6B", "6B", "5B", "5B", "4B", "4B", "3B", "3B", "2B",
    "2B", "1B", "1B", "0B"
]
fosse = []
mainJoueur = []
mainIA = []

# ----Display---- #


def display(index):
    input_str = {
        1: "La carte piochée à été posée",
        2: f"Carte posée : {fosse[-1]}",
        3: "Vous piochez",
        4: "L'IA pioche",
        5: "Joueur gagne",
        6: "IA gagne",
    }
    output = 0
    print("|********************** UNO **********************|")
    print()
    print('Michel'.center(50))
    print(f"{len(mainIA)} cartes restantes".center(50))
    print()
    print()
    print()
    print(f"Fosse : {fosse[-1]}".center(50))
    print()
    print()
    print()
    print(f"{mainJoueur}".center(50))
    if index < 7:
        print(input_str[index].center(50))
    elif index == 7:
        output = str(input('Carte a jouer :'))
    print()
    print()
    print("|********************** *** **********************|")
    return output


def piocher(main):
    main.append(pioche.pop())
    if jouable(main):
        fosse.append(main.pop())
        display(1)
    elif main == mainIA:
        display(4)
    elif main == mainJoueur:
        display(3)


def jouable(main):
    cartejouable = []
    for carte in main:
        chiffreia = carte[0]
        lettreia = carte[1]
        cartedefosse = fosse[-1]
        chiffref = cartedefosse[0]
        lettref = cartedefosse[1]
        if chiffreia == chiffref or lettreia == lettref:
            cartejouable.append(carte)
    return cartejouable


def tourIA(main):
    cartes = jouable(main)
    if cartes:
        random.shuffle(cartes)
        fosse.append(main.pop(main.index(cartes[-1])))
        display(2)
    else:
        piocher(main)


def tour(main):
    if jouable(main):
        carte = display(7)
        fosse.append(main.pop(main.index(carte)))
        display(2)
    else:
        piocher(main)


def partie():
    lap = 0
    while mainJoueur or mainIA:
        if len(mainJoueur) >= 1 and lap == 0:
            tour(mainJoueur)
            lap = 1
        elif len(mainJoueur) < 1:
            display(5)
            break
        elif len(mainIA) >= 1 and lap == 1:
            tourIA(mainIA)
            lap = 0
        elif len(mainIA) < 1:
            display(6)
            break


def start():
    random.shuffle(pioche)
    for i in range(0, 2):
        mainJoueur.append(pioche.pop())
        mainIA.append(pioche.pop())
    fosse.append(pioche.pop())
    partie()


start()