import numpy as np
def print_matrix(name, matrix):
    print(f"Матриця {name}: \n{matrix}\n")


A = np.array([[-3, 1],[2, 1]])
A3 = np.dot(np.dot(A,A),A) 
result = 3 * A3 - 4 * A

print("Завдання 2.1.9")
print("Матриця A:\n "
      , A)
print("f(x) = 3*x^3 - 4*x\n")
print("Відповідь: \n"
      , result)

print("--------------------------")