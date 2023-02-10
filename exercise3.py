import string

def is_pangram(sentence, alphabet=string.ascii_lowercase):
    # convert the sentence to lowercase
    sentence = sentence.lower()
    # create a set of all letters of the alphabet
    alphabet = set(alphabet)
    # iterate through each character in the sentence
    for char in sentence:
        # remove the character from the set if it is in the alphabet
        alphabet.discard(char)
    # if the set is empty, then all letters of the alphabet were used
    return not alphabet

def main():
    try:
        sentence = input("Enter a sentence: ")
    except Exception as e:
        print("An error occurred:", e)
        return

    if is_pangram(sentence):
        print("The sentence is a pangram.")
    else:
        print("The sentence is not a pangram.")

if __name__ == "__main__":
    main()
