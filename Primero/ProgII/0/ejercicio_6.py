def imprime_consec(n: int) -> None:
    if (n == 1):
        print(n)
        return
    print(n)
    return imprime_consec(n - 1)

imprime_consec(10)
