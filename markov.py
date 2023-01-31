"""Generate Markov text from text files."""

from random import choice

# text = f.read('green-eggs.txt')


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text = open(file_path).read()
    print(text)
    
    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words_list = text_string.split()


    # your code goes here
    for i in range(len(words_list)-1):
        if i+2 <= len(words_list)-1:
            if (words_list[i], words_list[i + 1]) not in chains:
                value_list=[]
                chains[(words_list[i], words_list[i + 1])] = list([words_list[i + 2]])
 #               print(chains)
            if (words_list[i], words_list[i + 1]) in chains:

                chains[(words_list[i], words_list[i + 1])] += ([words_list[i + 2]])
        else:
            continue
    print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)



