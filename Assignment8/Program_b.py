# M = P.L.U
import numpy as np
import random


class Matrix:
    def mat_input(self):
        try:
            self.mat_len = int(input("Order of matrix (Hit enter to take a random matrix): "))
            print("Enter matrix elements: ")
            self.matrix = np.empty((self.mat_len, self.mat_len))
            for i in range(self.mat_len):
                for j in range(self.mat_len):
                    self.matrix[i, j] = float(input(f"A{i + 1}{j + 1}: "))
        except ValueError:
            print("\nRandom matrix taken!!!")
            self.mat_len = random.randint(2, 5)
            self.matrix = np.empty((self.mat_len, self.mat_len))
            for i in range(self.mat_len):
                for j in range(self.mat_len):
                    self.matrix[i, j] = random.randint(-10, 10)
            print(self.matrix)

    def pivote_pi(self, i_val):  # Function for pivoting and generating permutation matrix Pi
        self.swap = 0
        self.pi = np.identity(self.mat_len)  # Initializing Pi
        for j_val in range(self.mat_len - i_val):
            if abs(self.matrix[j_val + i_val, i_val]) == max(
                    abs(self.matrix[i_val:, i_val])):  # Finding row containing the largest element
                self.matrix[[i_val, j_val + i_val]] = self.matrix[[j_val + i_val, i_val]]  # Pivoting
                if j_val + i_val != i_val:  # To count number of swaps
                    self.swap = 1
                self.pi[[i_val, j_val + i_val]] = self.pi[[j_val + i_val, i_val]]  # Generating Pi

    def eliminate_li(self, i_val):  # For elimination and Li
        self.li = np.identity(self.mat_len)  # Initializing Li
        for j_val in range(self.mat_len - i_val - 1):
            fact = (self.matrix[i_val + j_val + 1, i_val]) / self.matrix[i_val, i_val]
            self.matrix[i_val + j_val + 1] -= (self.matrix[i_val] * fact)  # Elimination
            self.li[i_val + j_val + 1, i_val] = fact  # Generating Li

    def lu_decompose(self):
        self.o_mat = self.matrix.copy()
        self.ptot = np.identity(self.mat_len)  # Initializing Ptot
        self.ltot = np.identity(self.mat_len)  # Initializing Ltot
        self.count = 0
        for i_val in range(self.mat_len):
            self.pivote_pi(i_val)
            self.count += self.swap
            self.ptot = np.matmul(self.ptot, self.pi)
            self.eliminate_li(i_val)
            self.ltot = np.matmul(self.pi, np.matmul(self.ltot, np.matmul(self.pi, self.li)))
        self.p, self.l, self.u = self.ptot, self.ltot, self.matrix

        print(f"P: \n{self.p}")
        print(f"L: \n{self.l}")
        print(f"U: \n{self.u}")
        print(f"Origin Matrix: \n{np.matmul(self.ptot, np.matmul(self.ltot, self.matrix))}")
        self.matrix = self.o_mat.copy()

    def lu_det(self):
        self.lu_decompose()
        det_p = np.power(-1, self.count)
        det_u = np.prod(np.diag(self.u))  # l not required as its diagonal contains 1s and hence its det = 1
        print(f"\nDeterminant: {round(det_u * det_p, 10)}")


# Matrix input
if __name__ == "__main__":
    my_mat = Matrix()
    my_mat.mat_input()
    my_mat.lu_decompose()
