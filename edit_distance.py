import stdarray
import stdio

# Read x and y.
x = stdio.readString()
y = stdio.readString()

# Create (M + 1) x (N + 1) matrix opt with elements initialized to 0, where
# M and N are lengths of x and y respectively.
M = len(x)
N = len(y)
opt = stdarray.create2D((M + 1), (N + 1), 0)

# Initialize bottom row opt[M][j] (0 <= j <= N) to 2 * (N - j).
# Initialize right column opt[i][N] (0 <= i <= M) to 2 * (M - i).
for i in range(N - 1, -1, -1):
    opt[M][i] = opt[M][i + 1] + 2

for j in range(M - 1, -1, -1):
    opt[j][N] = opt[j + 1][n] + 2

# Compute the rest of opt.
a1 = 0
b2 = 0

for j in range(N - 1, -1, -1):
    for i in range(M - 1, -1, -1):
        if(x[i] == y[j]):
            opt[i][j] = opt[i + 1][j + 1]
        else:
            val = opt[i + 1][j + 1] + 1
            emptyX = opt[i][j + 1] + 2
            emptyY = opt[i + 1][j] + 2
            opt[i][j] = min(min(emptyX, emptyY, val)

stdio.writeln(x)

stdio.writeln(y)
stdio.writeln(str(M + 1) + " " + str(N + 1))
for i in range(0, M + 1):
    for j in range(0, N + 1):
        if j < N:
            stdio.writef("%3d ", opt[i][j])
        else:
            stdio.writef("%3d\n", opt[i][j])
