def plusMinus(arr):
    # negative = []
    # positie = []
    # zero = []
    # for digit in arr:
    #     if digit < 0:
    #         negative.append(digit)
    #     elif digit == 0:
    #         zero.append(digit)
    #     else:
    #         positie.append(digit)
    #
    # negative_ratio = len(negative)/len(arr)
    # positie_ratio = len(positie)/len(arr)
    # zero_ratio = len(zero)/len(arr)
    #
    # print(positie_ratio)
    # print(negative_ratio)
    # print(zero_ratio)

    print(format(len([x for x in arr if x > 0])/len(arr), ".6f"))
    print(format(len([x for x in arr if x < 0])/len(arr), ".6f"))
    print(format(len([x for x in arr if x == 0])/len(arr), ".6f"))



if __name__ == '__main__':
    n = float(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)