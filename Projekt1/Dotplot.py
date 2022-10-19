import os
import matplotlib.pyplot as plt
import pandas as pd
os.chdir(os.getcwd())
filename = "4YCO_D"
file = open("Data/"+filename, "r")
sequence = file.readline().strip()
brackets = file.readline().strip()

pairs = ["GC", "CG", "TA", "AT", "UA", "AU"]
print(sequence)
print(brackets)

Y = list(sequence)
X = list(sequence)
matrix = [[0]*len(X)]*len(Y)
for i in range(len(X)):
    for j in range(len(Y)):
        if X[i]+Y[j] in pairs:
            matrix[i][j] = 1

print(matrix)
plt.scatter()
plt.ylabel(filename)
plt.xlabel(filename)
plt.show()
