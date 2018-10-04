"""Analyze the word frequencies in a book downloaded from Project Gutenberg."""

import string


def get_word_list(file_name):
    """Read the specified project Gutenberg book.

    Header comments, punctuation, and whitespace are stripped away. The function
    returns a list of the words used in the book as a list. All words are
    converted to lower case.
    """

    lines = f.readlines()
    curr_line = 0
    while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
        curr_line += 1
    lines = lines[curr_line+1:]
    separators = string.punctuation + string.whitespace
    allwords = []
    for i in lines:
        i = i.replace("-", " ")
        for word in i.split(' '):
            oneword = word.strip(separators)
            oneword = oneword.lower()
            if oneword == '':
                pass
            else:
                allwords.append(oneword)
    return allwords

def get_top_n_words(word_list, n):
    """Take a list of words as input and return a list of the n most
    frequently-occurring words ordered from most- to least-frequent.

    Parameters
    ----------
    word_list: [str]
        A list of words. These are assumed to all be in lower case, with no
        punctuation.
    n: int
        The number of words to return.

    Returns
    -------
    int
        The n most frequently occurring words ordered from most to least.
    frequently to least frequentlyoccurring
    """
    word_counts = {}
    for word in word_list:
        word_counts[word] = word_counts.get(word, 0) + 1
    ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)
    return ordered_by_frequency[:n]


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    f = open("pg32325.txt", 'r')
    print(get_top_n_words(get_word_list(f), 10))
