
# Author : @jimmg35
# using python typing module for static check
# python 3.7.3

from typing import List, Tuple

data: List[List[str]] = [["■", "■", "□", "□", "■", "■", "□"],
                         ["□", "□", "■", "□", "□", "■", "■"],
                         ["■", "□", "□", "■", "■", "□", "□"],
                         ["□", "□", "□", "■", "□", "■", "□"],
                         ["■", "■", "□", "■", "□", "■", "■"]]


def getShape(matrix: List[List[str]]) -> List[int]:
    # return row, col of a matrix
    return [len(matrix), len(matrix[0])]


def Transpose(A) -> List[List[str]]:
    # transpose a matrix
    shape_A: List[int] = getShape(A)
    if shape_A[0] != 1:
        result: List[List[str]] = []
        for i in range(0, shape_A[1]):
            v: List[str] = []
            for j in range(0, shape_A[0]):
                v.append(A[j][i])
            result.append(v)
        return result
    else: #if A is row matrix
        return [[A[i]] for i in range(0, len(A))]




if __name__ == '__main__':
    data_T: List[List[str]] = Transpose(data)

    # main algorithm
    output: List[List[str]] = []
    for i in data_T:
        blank: List[str] = []
        solid: List[str] = []
        for j in i:
            if j == "■":
                solid.append(j)
            else:
                blank.append(j)
        output.append(blank + solid)
    print(Transpose(output))



    # [["■", "■", "□", "□", "■", "■", "□"],
    #  ["□", "□", "■", "□", "□", "■", "■"],
    #  ["■", "□", "□", "■", "■", "□", "□"],
    #  ["□", "□", "□", "■", "□", "■", "□"],
    #  ["■", "■", "□", "■", "□", "■", "■"]]

             # Gravity on!!~~~

    # [['□', '□', '□', '□', '□', '□', '□'], 
    #  ['□', '□', '□', '□', '□', '■', '□'], 
    #  ['■', '□', '□', '■', '□', '■', '□'], 
    #  ['■', '■', '□', '■', '■', '■', '■'], 
    #  ['■', '■', '■', '■', '■', '■', '■']]
        

    