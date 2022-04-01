# words.py
# Give a sentence and find the number of words

def main():
    sentence = input("Please enter a sentence: ")

    word_list= sentence.split()

    numWords = len(word_list)
    print(word_list)
    print(f"Number of words in the given sentence is: {numWords}")

main()