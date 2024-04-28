import random

def getWords(filename):
    try:
        with open(filename, 'r') as file:
            words = file.readlines()
        # Strip newline characters and convert list to tuple
        words = tuple(word.strip() for word in words)
        return words
    except FileNotFoundError:
        print("File not found.")
        return ()

articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
verbs = getWords("verbs.txt")
prepositions = getWords("prepositions.txt")

def sentence():
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())


if __name__ == "__main__":
    main()

