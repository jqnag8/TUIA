# Se propone una represetación como
# (número, palo)


def verifica_poker(
    carta_1: tuple[int, str],
    carta_2: tuple[int, str],
    carta_3: tuple[int, str],
    carta_4: tuple[int, str],
    carta_5: tuple[int, str],
):

    return carta_1[0] == carta_2[0] == carta_3[0] == carta_4[0] == carta_5[0]
