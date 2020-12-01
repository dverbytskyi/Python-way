import re
from collections import Counter

def count_words(file):
    with open(file, "r") as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print("Total words: {}".format(len(all_words)))
        print("========================")

        word_count = Counter()
        for word in all_words:
            word_count[word] += 1

        print("Top 20 words: ")
        for word in word_count.most_common(20):
            print(word[0], '\t', word[1])


if __name__ == "__main__":
    count_words("shakespeare.txt")





