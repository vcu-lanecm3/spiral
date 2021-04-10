def spiralize(number):
    if number == 1:
        return 1
    else:
        return (4 * number * number) - (6 * number) + 6 + spiralize(number - 2)
