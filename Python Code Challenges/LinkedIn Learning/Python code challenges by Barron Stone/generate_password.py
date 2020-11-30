import secrets

def generate_passphrase(number_of_words):
    with open('diceware.wordlist.asc', 'r') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for i in range(number_of_words)]
    return ' '.join(words)



if __name__ == "__main__":
    print(generate_passphrase(10))