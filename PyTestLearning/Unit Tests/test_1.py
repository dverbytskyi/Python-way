def find_numbers(start, number, end):
    list_1 = list()
    for nmb in range(start, end):
        if nmb // number == 0:
            list_1.append(nmb)

    return list_1

def find_numbers_1(start, number, end):
    list_1 = list()
    for nmb in range(start, end):
        if str(number) in str(nmb):
            list_1.append(nmb)

    return list_1

def find_numbers_2(start, number, end):
    list_1 = list()
    for nmb in range(start, end):
        if str(number) in str(nmb):
            list_1.append(nmb)

    return list_1

print(find_numbers_2(5, 5, 150))
