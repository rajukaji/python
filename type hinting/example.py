def return_positive_integer(float1: float, int2: int) -> int:
    # float type and int type parameters, with return type being int type
    return float1 if float1 > 0 else int2


value = return_positive_integer(3.4, -2)

print(value)