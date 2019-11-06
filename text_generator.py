
import stdio
import sys
from markov_model import MarkovModel


def main():
    k = int(sys.argv[1])
    T = int(sys.argv[2])
    text = sys.stdin.read()
    kgram = text[:k]
    model = markov_model(text, k)
    print model.gen(kgram, T)


if __name__ == '__main__':
    main()
