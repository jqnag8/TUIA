# 1) 30 | f(15, 3) -> 15 | f(5, 3) -> f(5, 4) -> f(5, 5) -> 5 f(1, 5) 
# 2) Muestra por pantalla 'x' si es múltiplo de 2. En caso de que no lo sea se le sumará +1 a 2 hasta encontrar su múltiplo.

def f_iter(n: int, d: int) -> None:
    while (n > 1):
        if (n % d == 0):
            print(n)
            n //= d
        else:
            d += 1

f_iter(30, 2)
