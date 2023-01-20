import secrets

pioche = [
    "9G", "9G", "8G", "8G", "7G", "7G", "6G", "6G", "5G", "5G", "4G", "4G",
    "3G", "3G", "2G", "2G", "1G", "1G", "0G", "9Y", "9Y", "8Y", "8Y", "7Y",
    "7Y", "6Y", "6Y", "5Y", "5Y", "4Y", "4Y", "3Y", "3Y", "2Y", "2Y", "1Y",
    "1Y", "0y", "9R", "9R", "8R", "8R", "7R", "7R", "6R", "6R", "5R", "5R",
    "4R", "4R", "3R", "3R", "2R", "2R", "1R", "1R", "0R", "9B", "9B", "8B",
    "8B", "7B", "7B", "6B", "6B", "5B", "5B", "4B", "4B", "3B", "3B", "2B",
    "2B", "1B", "1B", "0B"
]
fosse = []

main = []
mainIA = []


def pioche(main):
    i = secrets.randbelow(76)
