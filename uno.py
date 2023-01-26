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


def piocher(main):
    main.append(pioche.pop())
    if jouable(main):
        fosse.append(main.pop())


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
        print(f"L'IA pose un {fosse[-1]}")
    else:
        piocher(main)
        print("L'IA pioche")


def tour(main):
    if jouable(main):
        print(f"Michel : {len(mainIA)} cartes restantes")
        print(f"Fosse : {fosse[-1]}")
        print(f"main : {main}")

        carte = str(input('Carte a jouer :'))
        fosse.append(main.pop(main.index(carte)))
    else:
        piocher(main)
        print("Vous piochez")


def partie():
    while mainJoueur or mainIA:
        if len(mainJoueur) >= 1:
            tour(mainJoueur)
        elif len(mainJoueur) <= 1:
            print("Joueur Gagne")
            break
        elif len(mainIA) >= 1:
            tourIA(mainIA)
        elif len(mainIA) <= 1:
            print("IA Gagne")
            break


def start():
    random.shuffle(pioche)
    for i in range(0, 2):
        mainJoueur.append(pioche.pop())
        mainIA.append(pioche.pop())
    fosse.append(pioche.pop())
    partie()


start()