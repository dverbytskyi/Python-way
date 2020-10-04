import math


''''
Умова if second == search_number or first == search_number: сфокусована для одно-двоцифрових чисел,
тому для скажімо трицифрового числа перший захід у рекурсивну функцію буде верифікувати першу і другу цифру справа, наступний - другу і третю.
причому для трицифрового числа перший цикл верифікація second == search_number буде невірна - буде верифікуватися двоцифрове число
'''

# def recursive_search(candidate, search_number):
#     first = candidate % 10
#     second = candidate // 10
#     if second == search_number or first == search_number:
#         return True
#     elif second >= 10:
#         return recursive_search(second, search_number)
#     else:
#         return False

def recursive_search(candidate, search_number):
    if search_number >= 10:
        first = candidate % 100
        second = candidate // 100
    else:
        first = candidate % 10
        second = candidate // 10
    if second == search_number or first == search_number or candidate == search_number:
        return True
    elif second >= 10:
        return recursive_search(second, search_number)
    else:
        return False

def find_numbers(start, number, end):
    list_numbers = [item for item in range(start, end+1) if recursive_search(item, number)]

    return list_numbers


# print(find_numbers(5, 7, 300))

# def check_candidate(candidate, control_number):
#     while candidate:
#         last_number = candidate // 10
#         candidate %= 10
#         if last_number == control_number:
#             return True
#     return False
#
#
# def find_numbers_1(start, number, end):
#     list_numbers = [item for item in range(start, end+1) if check_candidate(item, number)]
#
#     return list_numbers


# print(find_numbers(5, 170, 6000))


# def recursive_search(candidate, search_number):
#     if search_number >= 10:
#         first = candidate % 100
#         second = candidate // 100
#     else:
#         first = candidate % 10
#         second = candidate // 10
#     if second == search_number or first == search_number or candidate == search_number:
#         return True
#     elif second >= 10:
#         return recursive_search(second, search_number)
#     else:
#         return False

# def isDigitPresent(candidate, number):
#     while candidate > 0:
#         if candidate % 10 == number:
#             break
#         candidate = candidate / 10
#     return candidate > 0
#
# def printNumbers(start, number, end):
#     for item in range(start, end + 1):
#         if item == number or isDigitPresent(item, number):
#             print(item, end=" ")
#
# printNumbers(5, 6, 600)
#
# def is_correct(number, search_number):
#     max_power = math.ceil(math.log10(number))
#
#     for item in range(1, max_power):
#         divider = 10 ** item
#         temp = number
#         while temp > 0:
#             if temp == search_number or temp % divider == search_number:
#                 return True
#             temp //= divider
#     return False

def check_number(item, to_check):
    if item > 0:
        max_power = int(math.log10(item)) + 1
    elif item == 0:
        max_power = 1
    else:
        max_power = int(math.log10(-item)) + 2

    # max_power = math.ceil(math.log10(item)) + 1 # обраховуєм скільчи цифр в числі

    while item > 0:
        for numb in range(0, max_power):
            part, remainder = divmod(item, 10**numb)  # вертаєм ціле і остаток від item // 2 and item % 2 as tuple
            if part == to_check or remainder == to_check:
                return True
        item //= 10

    return False

# def check_number(number, to_check):
#     max_power = math.ceil(math.log10(number)) + 1
#
#     while number > 0:
#         for i in range(1, max_power+1):
#             part, remainder = divmod(number, 10**i)
#             if part == to_check or remainder == to_check:
#                 return True
#         number //= 10
#
#     return False

def find_numbers_1(start, number, end):
    list_numbers = [item for item in range(start, end+1) if check_number(item, number)]

    return list_numbers

print(find_numbers_1(1, 132, 13000))


# max_power = len(48228)
# print(max_power)