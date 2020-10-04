def func(start, finish):
    while start < finish:
        yield start * start
        start += 1

asquare = func(1, 5)
for item in asquare:
    print(item)