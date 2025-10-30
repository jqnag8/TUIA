def balanceado(exp: str) -> bool:
    """Recibe una expresión matemática y devuelve True si los paréntesis (),
    corchetes [] y llaves {} están correctamente balanceados"""
    init_par: int = 0
    init_llaves: int = 0
    init_corch: int = 0

    for caracter in exp:
        match caracter:
            case "(":
                init_par += 1
            case ")":
                if init_par > 0:
                    init_par -= 1
                else:
                    return False
            case "{":
                init_llaves += 1
            case "}":
                if init_llaves > 0:
                    init_llaves -= 1
                else:
                    return False
            case "[":
                init_corch += 1
            case "]":
                if init_corch > 0:
                    init_corch -= 1
                else:
                    return False

    if init_corch + init_llaves + init_par == 0:
        return True
    else:
        return False


# ----- TEST -----
def test_balanceado():
    assert balanceado("(x+y)/2") == True
    assert balanceado("[8*4(x+y)] + {2+5}") == True
    assert balanceado("(x+y]/2") == False
    assert balanceado("2)(x+y)") == False
