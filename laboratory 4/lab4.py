# 1.
# Write a Python class that simulates a Stack. The class should implement methods like push, pop, peek (the last two
# methods should return None if no element is present in the stack).

class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if len(self.elements) > 0:
            popped_element = self.elements[-1]
            del self.elements[-1]
            return popped_element
        else:
            return None

    # peek - The element retrieved does not get deleted or removed from the Stack.
    def peek(self):
        if len(self.elements) > 0:
            return self.elements[-1]
        else:
            return None

    def __str__(self):
        return f"\nMy stack: {self.elements} \nStack size: {len(self.elements)}"


my_Stack = Stack()
my_Stack.push(1)
my_Stack.push(2)
my_Stack.push(3)

print("-----Ex 1-----")
print(my_Stack)
print("Peek:", my_Stack.peek())
print("Pop:", my_Stack.pop())
print("Peek:", my_Stack.peek())
print("Pop:", my_Stack.pop())
print("Peek:", my_Stack.peek())
print("Pop:", my_Stack.pop())
print("Peek:", my_Stack.peek())
print("Pop:", my_Stack.pop())

# 2. Write a Python class that simulates a Queue. The class should implement methods like push, pop, peek (the last
# two methods should return None if no element is present in the queue).


class Queue:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if len(self.elements) > 0:
            popped_element = self.elements[0]
            self.elements = self.elements[1:]
            return popped_element
        else:
            return None

    # peek - The element retrieved does not get deleted or removed from the Queue.
    def peek(self):
        if len(self.elements) > 0:
            return self.elements[0]
        else:
            return None

    def __str__(self):
        return f"\nMy queue: {self.elements} \nQueue size: {len(self.elements)}"


my_Queue = Queue()
my_Queue.push(1)
my_Queue.push(2)
my_Queue.push(3)

print("\n-----Ex 2-----")
print(my_Queue)
print("Peek:", my_Queue.peek())
print("Pop:", my_Queue.pop())
print("Peek:", my_Queue.peek())
print("Pop:", my_Queue.pop())
print("Peek:", my_Queue.peek())
print("Pop:", my_Queue.pop())
print("Peek:", my_Queue.peek())
print("Pop:", my_Queue.pop())

# 3. Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization. The class
# should provide methods to access elements (get and set methods) and some mathematical functions such as transpose,
# matrix multiplication and a method that allows iterating through all elements form a matrix an apply a
# transformation over them (via a lambda function).


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for _ in range(n)]

    def get_element(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.m:
            return self.matrix[i][j]
        else:
            return None

    def set_element(self, i, j, value):
        if 0 <= i < self.n and 0 <= j < self.m:
            self.matrix[i][j] = value
        else:
            return None

    def transpose(self):
        transposed_matrix = [[0] * self.n for _ in range(self.m)]
        for i in range(self.n):
            for j in range(self.m):
                transposed_matrix[j][i] = self.matrix[i][j]
        return transposed_matrix

    def matrix_multiplication(self, second_matrix):
        if self.m != len(second_matrix):
            print("Can't multiply these matrices - the number of columns in a matrix must be equal to the number of "
                  "rows in the other matrix")
            return None

        result = []
        for _ in range(self.n):
            row = [0] * len(second_matrix[0])
            result.append(row)

        for i in range(self.n):
            for j in range(len(second_matrix[0])):
                for k in range(self.m):
                    result[i][j] += self.matrix[i][k] * second_matrix[k][j]

        return result

    def apply_transformation(self, transformation_function):
        for i in range(self.n):
            for j in range(self.m):
                self.matrix[i][j] = transformation_function(self.matrix[i][j])

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str


my_Matrix = Matrix(2, 4)

my_Matrix.set_element(0, 0, 1)
my_Matrix.set_element(0, 1, 2)
my_Matrix.set_element(0, 2, 3)
my_Matrix.set_element(0, 3, 4)
my_Matrix.set_element(1, 0, 5)
my_Matrix.set_element(1, 1, 6)
my_Matrix.set_element(1, 2, 7)
my_Matrix.set_element(1, 3, 8)

print("\n-----Ex 3-----")
print("\nOriginal Matrix:")
print(my_Matrix)

transposed_matrix = Matrix(my_Matrix.m, my_Matrix.n)
transposed_matrix.matrix = my_Matrix.transpose()

print("Transposed Matrix:")
print(transposed_matrix)

my_Matrix.apply_transformation(lambda x: x * 2)
print("Matrix after Transformation:")
print(my_Matrix)

matrix1 = Matrix(2, 3)
matrix2 = Matrix(3, 2)
matrix1.set_element(0, 0, 1)
matrix1.set_element(0, 1, 2)
matrix1.set_element(0, 2, 2)
matrix1.set_element(1, 0, 4)
matrix1.set_element(1, 1, 3)
matrix1.set_element(1, 2, 1)

matrix2.set_element(0, 0, 1)
matrix2.set_element(0, 1, 1)
matrix2.set_element(1, 0, 2)
matrix2.set_element(1, 1, 3)
matrix2.set_element(2, 0, 4)
matrix2.set_element(2, 1, 2)

print("First Matrix:")
print(matrix1)
print("Second Matrix:")
print(matrix2)

multiplication_result = matrix1.matrix_multiplication(matrix2.matrix)

print("Matrix Multiplication Result:")
result = Matrix(len(multiplication_result), len(multiplication_result[0]))
result.matrix = multiplication_result
print(result)



