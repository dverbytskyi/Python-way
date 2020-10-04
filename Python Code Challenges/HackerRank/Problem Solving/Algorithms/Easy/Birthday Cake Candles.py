def birthdayCakeCandles(candles):
    max_value = max(candles)
    res = candles.count(max_value)
    # res = list((candles.count(i)) for i in candles)
    return res

if __name__ == '__main__':

    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))

    print(birthdayCakeCandles(candles))