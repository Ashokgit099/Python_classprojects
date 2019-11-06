import stdarray
import stdio

# Read x, y, and opt from standard input.

x = stdio.readString()
y = stdio.readString()
opt = stdarray.readInt2D()

# Compute M and N.
M = len(x)
N = len(y)

# Write edit distance between x and y.
stdio.writef("Edit distance = %d\n", str(opt[0][0]))

# Recover and write an optimal alignment.
i = 0
j = 0

while i != M and j != N:
    if opt[i][j] == opt[i + 1][j] + 2:
        stdio.writeln(x[i] + " - 2")
        i += 1
    elif opt[i][j] == opt[i][j + 1] + 2:
        stdio.writeln("- " + y[j] + " 2")
        j += 1
    elif x[i] == y[j]:
        stdio.writeln(x[i] + " " + y[j] + " 0")
        i += 1
        j += 1
    elif x[i] != y[j]:
        stdio.writeln(x[i] + " " + y[j] + " 1")
        i += 1
        j += 1
    if i == M and j == N-1:
        stdio.writeln("- " + y[j] + " 2")
    elif i == M - 1 and j == N:
        stdio.writeln(x[i] + " -2")
