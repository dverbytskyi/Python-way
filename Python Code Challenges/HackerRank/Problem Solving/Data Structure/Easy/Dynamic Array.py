def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]
    lastAnswer = 0
    res = list()
    print(seqList)
    for q in queries:
        index = (q[1] ^ lastAnswer) % n
        if q[0] == 1:
            seqList[index].append(q[2])
        else:
            position = q[2] % len(seqList[index])
            lastAnswer = seqList[index][position]
            res.append(lastAnswer)

    print(res)
    return res



if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)