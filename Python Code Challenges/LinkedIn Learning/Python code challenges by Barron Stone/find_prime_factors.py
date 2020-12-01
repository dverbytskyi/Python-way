import math

def get_prime_factors(input_number):
    prime_numbers = []
    if input_number > 1:
        for prime in range(2, input_number):
            if input_number % prime == 0:
                print(input_number, " is not a prime number")
                print(prime, "times", input_number//prime, "is", input_number)
                prime_numbers.append(prime)
            # print(prime)
    else:
        print(input_number, " is not a prime number")

    return prime_numbers

# get_prime_factors(630)

def get_prime_factors_2(input_number):
    prime_numbers = []

    while input_number % 2 == 0:
        input_number = input_number / 2
        print(input_number)

    for number in range(3, int(math.sqrt(input_number))+1, 2):
        # print(number)
        while input_number % number == 0:
            print(number)
            input_number = input_number / number

    if input_number > 2:
        print(input_number)

    # return prime_numbers

# get_prime_factors_2(630)

def get_prime_factors_3(input_number):
    prime_numbers = list()
    divisor = 2
    while divisor <= input_number:
        if (input_number % divisor) == 0:
            prime_numbers.append(divisor)
            input_number = input_number / divisor
        else:
            divisor += 1
    return prime_numbers


print(get_prime_factors_3(13))