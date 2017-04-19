import numpy as np
import fileinput

def one():
    M1 = np.array([[2, 5], [1, -10]])
    v1 = np.array([1, 3])
    answer = np.linalg.solve(M1, v1)
    print(answer)

def fouth():
    rows = []
    for line in fileinput.input():
        rows.append([float(i) for i in line.split()])
    M1 = np.array([[2, 5], [1, -10]])
    print(M1)

if __name__ == '__main__':
    fouth()
