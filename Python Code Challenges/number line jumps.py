def kangaroo(x1, v1, x2, v2):
    # while x1 < x2:
    #     if v2 > v1:
    #         print('NO')
    #         break
    #     x1 += + v1
    #     x2 += v2
    #     if x1 == x2:
    #         print('YES')
    #         break
    #     elif x1 > x2:
    #         print('NO')
    #         break
    response = 'NO'
    if v2 < v1:
        if (x1 - x2) % (v2 - v1) == 0:
            response = 'YES'
    return response

if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
