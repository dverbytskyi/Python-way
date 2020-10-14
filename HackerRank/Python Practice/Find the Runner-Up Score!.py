if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr_set = set(arr)
    arr_array = list(arr_set)
    arr_array.remove(max(arr))
    print(max(arr_array))