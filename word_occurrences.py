"""
CP1404 Practical 05 World Occurrences
This program count the occurrences of words in a string
"""


def main():
    text = input("Text: ")  # read user input
    text_dic = create_dictionary(text)  # create dictionary based on user input
    print_dictionary(text_dic)  # print the dictionary according to specific format


def print_dictionary(text_dic):
    for word in text_dic:
        print("{:<11}: {}".format(word, text_dic[word]))


def create_dictionary(text):
    texts = text.split()
    texts.sort()
    text_dic = {}  # create an empty dictionary for text
    for word in texts:
        if word not in text_dic:
            text_dic[word] = 1  # create new key and item if a word not already exists
        else:
            text_dic[word] += 1
    return text_dic


main()
