import math
import stdio


# Reads in the displacements produced by bead_tracker.py from standard
# input; computes an estimate of Boltzmann's constant and Avogadro's number;
# and writes those estimates to standard output.
def main():
    P = 0.5 * (10 ** -6)
    R = 8.31457
    N = 9.135 * (10 ** -4)
    T = 297
    PiToMe = 0.175 * (10 ** -6)
    radilaDis = []
    while not stdio.isEmpty():
        radilaDis += [stdio.readFloat()]
    self_diffusion = 0.0
    for r in radilaDis:
        self_diffusion += (r * PiToMe) ** 2
    self_diffusion /= (2 * len(radilaDis))
    boltzman = (6 * math.pi * self_diffusion * N * P) / T
    avogadro = (R / boltzman)
    stdio.writef("Boltzman = %.6e\n", boltzman)
    stdio.writef("Avogadro = %.6e\n", avogadro)


if __name__ == '__main__':
    main()
