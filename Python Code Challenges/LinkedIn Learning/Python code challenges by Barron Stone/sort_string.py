
def sort_words(input_string):
    words = input_string.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)


print(sort_words("banana ORANGE apple"))