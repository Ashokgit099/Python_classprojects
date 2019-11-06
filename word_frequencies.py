import operator
import stdio
import sys


# Return a list containing the keys of the dictionary st in
# reverse order of the values of the dictionary.
def keys(st):
    a = sorted(st.items(), key=operator.itemgetter(1),
               reverse=True)
    return [v[0] for v in a]


# Return a dictionary whose keys are the words from the given
# list of words and values are the corresponding frequencies.
def count_word_frequencies(words):
    # Initialize st to an empty dictionary.
    st = {}

    # Iterate over each word w in words.
    for i in words:
        # Add w with frequency 0 to st using the
        # st.setdefault() method.
        # Increment the frequency of w by 1.

        st[str(i)] = st.get(i, 0) + 1

    # Return st.
    return st


# Write (in reverse order of values) the key-value pairs of
# the dictionary st to standard output, one per line, and with
# a ' -> ' between a key and the corresponding value.
def write_word_frequencies(st):
    # Initialize words to the keys in st in reverse order of
    # the values (frequencies).
    st2 = keys(st)

    # Iterate over each word w in words.
    for i in range(len(st2)):
        # Write w and its frequency with a ' -> ' between
        # the two.
        stdio.write((st2[i] + ' -> '))
        stdio.writeln(st[st2[i]])


# Test client [DO NOT EDIT].
def _main():
    words = stdio.readAllStrings()
    write_word_frequencies(count_word_frequencies(words))


if __name__ == '__main__':
    _main()
