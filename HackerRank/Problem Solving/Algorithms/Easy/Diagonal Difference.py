
def diagonalDifference(arr):
    primary_diagonal, secondary_diagonal = 0, 0
    for dig in range(len(arr)):
        primary_diagonal += arr[dig][dig]
        secondary_diagonal += arr[dig][-dig-1]

    return abs(primary_diagonal - secondary_diagonal)

n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)