"""
## Intro to python exercises shell code

"""
# Find odd or even
def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if x%2 == 0:
        return False
    else:
        return True


def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    list_of_letters = []
    for i in word:
        list_of_letters.append(i)
    word_len= len(list_of_letters)
    m = divmod(word_len, 2)[0]
    for j in range(m+1):
        if list_of_letters[j] != list_of_letters[-1-j]:
            print('{} is not spelled the same forwards and backwards'.format(word))
        elif j == m:
            print('{} is spelled the same forwards and backwards'.format(word))


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    new_list = []
    for i in range(len(numlist)-1):
        if numlist[i]%2 != 0:
            new_list.append(numlist[i])
    return new_list


def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    import re
    
    word_dict = {}
    words_list = re.split(' |\n', text)
    print(words_list)
    #keys = set(words_list)
    #print(keys)
    #for k in keys:
    for w in words_list:
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1
    return word_dict