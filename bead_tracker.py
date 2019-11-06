import stdio
import sys
from blob_finder import BlobFinder
import contextlib
from picture import Picture


# Takes an integer P, a float tau, a float delta, and a sequence of JPEG
# filenames as command-line arguments; identifies the beads in each JPEG
# image using BlobFinder; and writes out (one per line, formatted with 4
# decimal places to the right of decimal point) the radial distance that
# each bead moves from one frame to the next (assuming it is no more than
# delta).
def main():
    P = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    pic = Picture(sys.argv[4])
    bf = BlobFinder(pic, tau)
    previousBlob = bf.getBeads(P)
    for i in range(5, len(sys.argv)):
        bf = BlobFinder(Picture(sys.argv[i]), tau)
        curBlob = bf.getBeads(P)
        for i in range(len(previousBlob)):
            some = float('inf')
            for j in range(len(curBlob)):
                Dist = previousBlob[i].distanceTo(curBlob[j])
                if Dist < some:
                    some = Dist
            if some < delta:
                stdio.writef("%.4f\n", some)
    stdio.writeln()
    previousBlob = curBlob


if __name__ == '__main__':
    main()
