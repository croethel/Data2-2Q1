def fibonacci(fin: float) -> float:
    """
    build a classic fibonacci function - No RECURSION
    """
    a = 0
    b = 1

    if fin >= 0:
        for i in range(1, fin, 1):
            c = a + b
            a = b
            b = c
        return c
