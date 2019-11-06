import stdio
import sys
from markov_model import MarkovModel


def main():
    k = int(sys.argv[1])
    s = sys.argv[2]
    t = sys.stdin.read()
    model = markov_model(t, k)
    stdio.writeln(model.replace_unknown(s))

if __name__ == '__main__':
    main()
