
def find_numbers(start, number, end):
    _list = list()
    for nmb in range(start, end):
        if number % 10 == 0:
            _list.append(nmb)

    return _list

print(find_numbers(0, 1, 150))
