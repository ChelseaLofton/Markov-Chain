"""Generate Markov text from text files."""

from random import choice
import sys

# text = f.read('green-eggs.txt')


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text = open(file_path).read()
 #   print(text)
    
    return text


def make_chains(text_string, n_count):
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
        if i+n_count <= len(words_list)-1:
            current_key = tuple(words_list[i:i+n_count])
            if current_key not in chains:
                chains[current_key] = list([words_list[i + n_count]])
            if current_key in chains:

                chains[current_key] += ([words_list[i + n_count]])
        else:
            continue
#    print(chains)
    return chains

#         for i in range(len(words_list)-1):
#           if i+n_count <= len(words_list)-1:
#             if (words_list[i], words_list[i + 1], words_list[i + 2]) not in chains:
#                 value_list=[]
#                 chains[(words_list[i], words_list[i + 1], words_list[i + 2])] = list([words_list[i + 3]])
#  #               print(chains)
#             if (words_list[i], words_list[i + 1]) in chains:

#                 chains[(words_list[i], words_list[i + 1])] += ([words_list[i + 2]])
#         else:
#             continue


def make_text(chains, n_count):
    """Return text from chains."""

    words = []
    while True:
        keys_list = list(chains.keys())
        link = choice(keys_list)
        first_char = link[0][0]
        print (first_char)
        if first_char.isupper() == True:

            nth_link = choice(chains[link])
            for i in range (len(link)-1):
                words.append(str(link[i]))
            words.append(str(nth_link))
            new_key = link[1:i+n_count] + (nth_link,)
            if new_key in chains:
                continue
            elif new_key not in chains:
                break
        elif link[0][0].isupper() == False:
            continue
    words= ' '.join(words)
    # print(words)
    return words


#input_path = 'adventure_time.txt'
input_path = str(sys.argv[1])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 4)

# Produce random text
random_text = make_text(chains, 4)

print(random_text)



