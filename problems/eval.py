def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))

print(basic_op('+', 3, 5))