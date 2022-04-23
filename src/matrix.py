"""
---------------------
MATRIX IMPLEMENTATION
---------------------

* Implements the matrix data-structure
* Create an instance of the 'Matrix' class to create one
* ...

"""


#import ...


class Matrix(object):
    """This is the class created to implement the matrix data-structure
Supports only matrices containing numbers (not strings!)

Argument 'data' must be of type 'list'
'data' must contain 'list' s depicting the rows
"""

    def __init__(self, data):
        if type(data) != list: raise Exception("Argument 'data' must be of type 'list'")
        if len(data) != 0:
            if type(data[0]) != list: raise Exception("Each row in the matrix must be of type 'list'")
            row_len = len(data[0])
            if row_len == 0: raise Exception("Rows of the matrix should not be empty")
            for row in data[1:]:
                if type(row) != list: raise Exception("Each row in the matrix must be of type 'list'")
                if len(row) != row_len: raise Exception("Irregular lengths of rows in the matrix")
                for ele in row:
                    if type(ele) not in (int, float):
                        raise Exception("Each element of the matrix must be of type 'int' or 'float'")
            self.data = data
            self.order = (len(data), row_len)
        else:
            self.data = []
            self.order = (0, 0)

    def get_data(self):
        """Returns a copy of the matrix in the form of nested lists"""

        return eval(str(self.data))

    def get_order(self):
        """Returns a copy of the order in the form of a tuple"""

        return eval(str(self.order))

    def get_row(self, row_num):
        """Returns a copy of the row required in the form of a list"""

        if (type(row_num) != int) or (row_num < 1) or (row_num > len(self.data)):
            raise Exception("Invalid row number")
        row = self.data[row_num - 1]
        return eval(str(row))

    def get_column(self, col_num):
        """Returns a copy of the column required in the form of a list"""

        if (type(col_num) != int) or (col_num < 1) or (col_num > len(self.data[0])):
            raise Exception("Invalid column number")
        col = []
        for row in self.data: col.append(row[col_num - 1])
        return eval(str(col))

    def get_determinant(self):
        """Returns the determinant of the matrix in float type"""

        if not(self.isSquareMatrix()):
            raise Exception("Determinant can only be calculated for square matrices")
        odr = self.order[0]
        if odr == 0: return 1.0
        elif odr == 1: return float(self.data[0][0])
        dtr = 0
        n = 1
        for ele in self.data[0]:
            dtr = dtr + (ele * self.get_cofactor(1, n))
            n += 1
        return dtr

    def get_minor(self, row_num, col_num):
        """Returns the minor of the element,
        Whose row number and column number should be given"""

        if not(self.isSquareMatrix()): raise Exception("Minor only exists for square matrices")
        odr = self.order[0]
        if odr == 0: raise Exception("Empty matrix doesn't have a minor")
        if (type(row_num) != int) or (row_num < 1) or (row_num > odr):
            raise Exception("Invalid row number")
        elif (type(col_num) != int) or (col_num < 1) or (col_num > odr):
            raise Exception("Invalid column number")
        if odr == 1: return 1.0
        data = []
        for r_n in range(0, odr):
            if r_n + 1 == row_num: continue
            data.append([])
            for c_n in range(0, odr):
                if c_n + 1 == col_num: continue
                data[-1].append(self.data[r_n][c_n])
        return Matrix(data).get_determinant()

    def get_cofactor(self, row_num, col_num):
        """Returns the cofactor of the element,
        Whose row number and column number should be given"""

        if not(self.isSquareMatrix()): raise Exception("Cofactor only exists for square matrices")
        odr = self.order[0]
        if odr == 0: raise Exception("Empty matrix doesn't have a cofactor")
        if type(row_num) != int: raise Exception("Invalid row number")
        if type(col_num) != int: raise Exception("Invalid column number")
        return ((-1) ** (row_num + col_num)) * self.get_minor(row_num, col_num)

    def isZeroMatrix(self):
        """Returns True if the matrix is a zero matrix, else False"""

        if self.order[0] == 0: return False
        for row in self.data:
            for ele in row:
                if ele != 0: return False
        return True

    def isRowMatrix(self):
        """Returns True if the matrix is a row matrix, else False"""

        return self.order[0] == 1

    def isColumnMatrix(self):
        """Returns True if the matrix is a column matrix, else False"""

        return self.order[1] == 1

    def isOrthogonalMatrix(self):
        """Returns True if the matrix is an orthogonal matrix, else False"""

        # Generating Identity matrix of required order
        I_data = []
        I_order = self.order[0]
        for r_n in range(I_order):
            I_data.append([])
            for c_n in range(I_order):
                if r_n == c_n: I_data[-1].append(1)
                else: I_data[-1].append(0)
        I = Matrix(I_data)
        #XXXXXXXXXXXXXXXXXXXXX
        return self * self.transpose() == I

    def isSquareMatrix(self):
        """Returns True if the matrix is a square matrix, else False"""

        if self.order[0] == self.order[1]: return True
        else: return False

    def isDiagonalMatrix(self):
        """Returns True if the matrix is a scalar matrix, else False"""

        if not(self.isSquareMatrix()): return False
        odr = self.order[0]
        if odr == 0: return True
        for r_n in range(odr):
            for c_n in range(odr):
                if r_n != c_n:
                    if self.data[r_n][c_n] != 0: return False
        return True

    def isScalarMatrix(self):
        """Returns True if the matrix is a scalar matrix, else False"""

        if not(self.isSquareMatrix()): return False
        odr = self.order[0]
        if odr == 0: return True
        val = self.data[0][0]
        for r_n in range(odr):
            for c_n in range(odr):
                if r_n == c_n:
                    if self.data[r_n][c_n] != val: return False
                else:
                    if self.data[r_n][c_n] != 0: return False
        #for n in range(odr):
        #    if self.data[n][n] != val: return False
        return True

    def isIdentityMatrix(self):
        """Returns True if the matrix is an identity matrix, else False"""

        if not(self.isSquareMatrix()): return False
        odr = self.order[0]
        for r_n in range(odr):
            for c_n in range(odr):
                if r_n == c_n:
                    if self.data[r_n][c_n] != 1: return False
                else:
                    if self.data[r_n][c_n] != 0: return False
        return True

    def isUpperTriangularMatrix(self):
        """Returns True if the matrix is an upper triangular matrix, else False"""

        if not(self.isSquareMatrix()): return False
        odr = self.order[0]
        for r_n in range(odr):
            for c_n in range(odr):
                if r_n > c_n:
                    if self.data[r_n][c_n] != 0: return False
        return True

    def isLowerTriangularMatrix(self):
        """Returns True if the matrix is a lower triangular matrix, else False"""

        if not(self.isSquareMatrix()): return False
        odr = self.order[0]
        for r_n in range(odr):
            for c_n in range(odr):
                if r_n < c_n:
                    if self.data[r_n][c_n] != 0: return False
        return True

    def isSingularMatrix(self):
        """Returns True if the matrix is a singular matrix, else False"""

        try: dtr = self.get_determinant()
        except: raise Exception("Singularity can only be checked for square matrices")
        return dtr == 0

    def isNonSingularMatrix(self):
        """Returns True if the matrix is a non-singular matrix, else False"""

        return not(self.isSingularMatrix())

    def isSymmetricMatrix(self):
        """Returns True if the matrix is a symmetric matrix, else False"""

        return self.transpose() == self

    def isSkewSymmetricMatrix(self):
        """Returns True if the matrix is a skew symmetric matrix, else False"""

        return self.transpose() == (self * -1)

    def __str__(self):
        temp_result = []
        slots = []
        for n in range(0, self.order[1]):
            slot_len = 0
            for r in self.data:
                ele_len = len(str(r[n]))
                if ele_len > slot_len: slot_len = ele_len
            slots.append(slot_len)
        for row in self.data:
            row_s = "| "
            for ele_n in range(0, self.order[1]):
                ele = row[ele_n]
                row_s = row_s + str(ele) + (" " * (slots[ele_n] - len(str(ele)) + 1))
            row_s += "|"
            temp_result.append(row_s)
        if len(self.data) == 0: return '[ ]'
        offset = " " * (len(temp_result[0]) - 4)
        result = "+-" + offset + "-+"
        for row_f in temp_result: result = result + '\n' + row_f
        result = result + '\n' + "+-" + offset + "-+"
        return result

    def __add__(self, other):
        if (type(other) != Matrix) or (self.order != other.get_order()):
            raise Exception("Only matrices of same order can be added")
        if self.order == (0, 0): return Matrix([])
        data = []
        data1 = self.data
        data2 = other.get_data()
        for r_n in range(0, self.order[0]):
            data.append([])
            for c_n in range(0, self.order[1]): data[-1].append(data1[r_n][c_n] + data2[r_n][c_n])
        return Matrix(data)

    def __sub__(self, other):
        if (type(other) != Matrix) or (self.order != other.get_order()):
            raise Exception("Only matrices of same order can be subtracted")
        if self.order == (0, 0): return Matrix([])
        data = []
        data1 = self.data
        data2 = other.get_data()
        for r_n in range(0, self.order[0]):
            data.append([])
            for c_n in range(0, self.order[1]): data[-1].append(data1[r_n][c_n] - data2[r_n][c_n])
        return Matrix(data)

    def __mul__(self, other):
        if type(other) != Matrix:
            if type(other) in (int, float):
                data = []
                for row in self.data:
                    data.append([])
                    for ele in row: data[-1].append(ele * other)
                return Matrix(data)
            else:
                raise Exception("Matrix can only be multiplied with int, float, and another matrix or itself")
        if self.order[1] != other.get_order()[0]:
            raise Exception(f"Matrix of order {str(self.order)} cannot be multiplied with matrix of order {str(other.get_order())}")
        data = []
        for row_n in range(0, len(self.data)):
            data.append([])
            for col_n in range(0, len(other.get_data()[0])):
                ele = 0
                row = self.data[row_n]
                col = other.get_column(col_n + 1)
                for n in range(0, len(row)):
                    term = row[n] * col[n]
                    ele += term
                data[-1].append(ele)
        return Matrix(data)

    def __pow__(self, other):
        if type(other) != int: raise Exception("'power' should only be int for '<matrix> ** <power>'")
        if other < 0: raise Exception("'power' should not be negative for '<matrix> ** <power>',\n try instead using the '.inverse()' method")
        if not(self.isSquareMatrix()): raise Exception("Only square matrices can be used with the 'power' operator ('**')")
        # Generating Identity matrix of required order
        I_data = []
        I_order = self.order[0]
        for r_n in range(I_order):
            I_data.append([])
            for c_n in range(I_order):
                if r_n == c_n: I_data[-1].append(1)
                else: I_data[-1].append(0)
        I = Matrix(I_data)
        #XXXXXXXXXXXXXXXXXXXXX
        result_matrix = I
        for n in range(other): result_matrix *= self
        return result_matrix

    def __eq__(self, other):
        if (type(other) != Matrix) or (self.order != other.get_order()):
            raise Exception("Only matrices of same order can be compared")
        #if self.order == (0, 0): return True
        #data1 = self.data
        #data2 = other.get_data()
        #for r_n in range(0, self.order[0]):
        #    for c_n in range(0, self.order[1]):
        #        if data1[r_n][c_n] != data2[r_n][c_n]: return False
        #return True
        return self.data == other.get_data()

    def transpose(self):
        """Returns the transpose of the matrix"""

        data = []
        for n in range(0, self.order[1]): data.append(self.get_column(n + 1))
        return Matrix(data)

    def adjoint(self):
        """Returns the adjoint of the matrix"""

        if not(self.isSquareMatrix()): raise Exception("Adjoint can only be calculated for square matrices")
        odr = self.order[0]
        temp_result_data = []
        for r_n in range(odr):
            temp_result_data.append([])
            for c_n in range(odr):
                temp_result_data[-1].append(self.get_cofactor(r_n + 1, c_n + 1))
        temp_result = Matrix(temp_result_data)
        return temp_result.transpose()

    def inverse(self):
        """Returns the inverse of the matrix"""

        if not(self.isSquareMatrix()): raise Exception("Inverse can only be calculated for square matrices")
        if self.isSingularMatrix(): raise Exception("Inverse doesn't exist for singular matrices")
        #odr = self.order[0]
        #if odr == 0: return self
        return self.adjoint() * (1 / self.get_determinant())


#def ...(...):


if __name__ == '__main__':
    print("This is the matrix module. Import this in your program and use the class 'Matrix'.")


# END
