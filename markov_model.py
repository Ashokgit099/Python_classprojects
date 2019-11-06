import stdio
import stdrandom
import sys


class MarkovModel(object):
    """
    Represents a Markov model of order k from a given text string.
    """

    def __init__(self, text, k):
        """
        Create a Markov model of order k from given text (assumed
        to have length at least k).
        """

        self._k = k
        self._st = {}
        circ_text = text + text[:k]
        for i in range(len(circ_text) - k):
            kgram = circ_text[i:i + k]
            next_char = circ_text[i + k]
            if kgram not in self._st:
                self._st[kgram] = {}
                self._st[kgram][next_char] = 1
            elif kgram in self._st and next_char not in self._st[kgram]:
                self._st[kgram][next_char] = 1
            elif kgram in self._st and next_char in self._st[kgram]:
                self._st[kgram][next_char] += 1

    def order(self):
        """
        Return order of Markov model.
        """

        return self._k

    def kgram_freq(self, kgram):
        """
        Return number of occurrences of kgram in text.
        """

        if self.k != len(kgram):
            raise ValueError('kgram' + kgram + 'not of length ' + str(self.k))

        if kgram not in self.st:
            return 0
        a = self.st[kgram].values()
        a = sum(a)
        return a

    def char_freq(self, kgram, c):
        """
        Return number of times character c follows kgram.
        """

        if self.k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' + str(self.k))

        if kgram not in self.st:
            return 0
        if c not in self.st[kgram]:
            return 0
        return self.st[kgram][c]

    def rand(self, kgram):
        """
        Return a random character following kgram.
        """

        if self.k != len(kgram):
            raise ValueError('kgram ' + kgram + ' not of length ' + str(self.k))

        if not kgram in self.st:
            raise ValueError('Unknown Kgram ' + kgram)
        ab = stdrandom.discrete(list(self._st[kgram].values()))
        x = list(kgram.keys())
        return x[ab]

    def gen(self, kgram, T):
        """
        Generate and return a string of length T by simulating a trajectory
        through the correspondng Markov chain. The first k (<= T) characters
        of the generated string is the argument kgram.
        """

        text = kgram
        while len(text) < T:
            text += self._rand(text[-self.order():])
        return text

    def replace_unknown(self, corrupted):
        """
        Replace unknown characters (~) in corrupted with most probablenb
        characters, and return that string.
        """

        # Return the index of the maximum element in the given list a.
        def argmax(a):
            return a.index(max(a))

        original = ''
        for i in range(len(corrupted)):
            if corrupted[i] == '~':
                kgram_before = corrupted[i - self._k + 1]
                kgram_after = corrupted[i + 1: i + self.k + 1]
                probs = []
                for hypothesis in hypothesis:
                    context = kgram_before + hypothesis + kgram_after
                    p = 1.0
                    for i in range (self._k + i):
                        kgram = context[i:self.k + i]
                        char = context[self._k + i]
                        if not (kgram in self._st.keys()) \
                            or not (char in self._st.keys()):
                            p = 0
                            break
                        else:
                            a = self._st[kgram].values()
                            abc = sum(self._st[kgram].values())
                            aap = (self._st[kgram][char] * 1.0 / abc * 1.0)
                            abc_probability = float(aap)
                            p *= abc_probability
                        probs.append(p)
                    max_probs = hypothesis[argmax(probs)]
                    original += max_probs
            else:
                original += corrupted[i]
        return original


def _main():
    """
    Test client [DO NOT EDIT].
    """

    text, k = sys.argv[1], int(sys.argv[2])
    model = MarkovModel(text, k)
    a = []
    while not stdio.isEmpty():
        kgram = stdio.readString()
        char = stdio.readString()
        a.append((kgram.replace("-", " "), char.replace("-", " ")))
    for kgram, char in a:
        if char == ' ':
            stdio.writef('freq(%s) = %s\n', kgram, model.kgram_freq(kgram))
        else:
            stdio.writef('freq(%s, %s) = %s\n', kgram, char,
                         model.char_freq(kgram, char))


if __name__ == '__main__':
    _main()
