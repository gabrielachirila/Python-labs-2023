# 1. Write a function to return a list of the first n numbers in the Fibonacci string.

def fibonacci_for_first_n(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        our_list = [0, 1]
        i = 2
        while i < n:
            our_list.append(our_list[i - 1] + our_list[i - 2])
            i += 1
        return our_list


print("-----Ex 1-----")
n = int(input("Enter n for Fibonacci: "))
print("Fibonacci for n = {} is: {}".format(n, fibonacci_for_first_n(n)))


# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.


def find_prime_numbers(list_of_numbers):
    prime_numbers = []
    for number in list_of_numbers:
        if number == 0 or number == 1 or number < 0:
            continue
        elif number == 2:
            prime_numbers.append(number)
        else:
            ok = 1
            for j in range(2, number - 1):
                if number % j == 0:
                    ok = 0
            if ok == 1:
                prime_numbers.append(number)
    return prime_numbers


print("-----Ex 2-----")
print("The prime numbers are: {}".format(find_prime_numbers(list(range(-200, 201)))))


# 3.Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited
# with b, a - b, b - a)


def lists_operations(a, b):
    intersection = [x for x in a if x in b]
    reunion = list(set(a + b))
    a_minus_b = [x for x in a if x not in b]
    b_minus_a = [x for x in b if x not in a]

    return intersection, reunion, a_minus_b, b_minus_a


print("-----Ex 3-----")
operations = lists_operations([0, 1, 2], [0, 5, 6])
print("Operations between two lists: intersection: {} , reunion: {} , a - b: {} , b - a: {}".format(operations[0], operations[1], operations[2], operations[3]))


# 4.Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and
# a start position (integer). The function will return the song composed by going through the musical notes beginning
# with the start position and following the moves given as parameter. Example : compose(["do", "re", "mi", "fa",
# "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]


def compose_song(musical_notes, moves, start_position):
    number_of_notes = len(musical_notes)
    song = [musical_notes[start_position]]

    for move in moves:
        new_position = (start_position + move) % number_of_notes
        song.append(musical_notes[new_position])
        start_position = new_position

    return song


print("-----Ex 4-----")
ex4 = compose_song(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
print("Composed song:", ex4)


# 5.Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the
# elements under the main diagonal with 0 (zero).


def zero_matrix(given_matrix):
    length = len(given_matrix)
    new_matrix = [row[:] for row in given_matrix]

    for i in range(length):
        for j in range(length):
            if i > j:
                new_matrix[i][j] = 0

    return new_matrix


print("-----Ex 5-----")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
ex5 = zero_matrix(matrix)
print("Modified matrix", ex5)


# 6.Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list
# containing the items that appear exactly x times in the incoming lists. Example: For the [1,2,3], [2,3,4],[4,5,6],
# [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.


def find_items(x, *lists):
    item_count = {}

    for lista in lists:
        for item in lista:
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1

    result = []
    for item, count in item_count.items():
        if count == x:
            result.append(item)

    return result


print("-----Ex 6-----")
x = 2
ex6 = find_items(x, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"])
print("Items that appear exactly {} time/s: {}".format(x, ex6))


# 7.Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element
# will be the greatest palindrome number.


def is_palindrome(number):
    aux_number = number
    reversed_number = 0

    while aux_number > 0:
        reversed_number = reversed_number * 10 + aux_number % 10
        aux_number //= 10

    if number == reversed_number:
        return True
    else:
        return False


def find_palindromes(list_of_numbers):
    count = 0
    greatest_palindrome = None

    for number in list_of_numbers:
        if is_palindrome(number):
            count += 1
            if greatest_palindrome is None or number > greatest_palindrome:
                greatest_palindrome = number

    return count, greatest_palindrome


print("-----Ex 7-----")
ex7 = find_palindromes([1221, 123, 11, 78987, 5678])
print("I found {} palindrome numbers, and the greater is {}".format(ex7[0], ex7[1]))


# 8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set
# to True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the
# flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.


def generate_list(list_of_strings, x=1, flag=True):
    result = []

    for string in list_of_strings:
        char_list = []

        for char in string:
            code = ord(char)
            if flag == True and code % x == 0:
                char_list.append(char)
            elif flag == False and code % x != 0:
                char_list.append(char)

        result.append(char_list)

    return result


print("-----Ex 8-----")
print("First exmple with ASCII code:", generate_list(["Ana", "are", "mere"], x=3))
print("Second example with ASCII code", generate_list(["Ana", "are", "mere"], x=3, flag=False))

print("Third exmple with ASCII code:", generate_list(["test", "hello", "lab002"], x=2, flag=False))


# 9.Write a function that receives as parameter a matrix which represents the heights of the spectators in a stadium
# and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the
# game. A spectator can't see the game if there is at least one taller spectator standing in front of him. All the
# seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the
# closest row from the field. Example:
# FIELD
# [[1, 2, 3, 2, 1, 1],
#  [2, 4, 4, 3, 7, 2],
#  [5, 5, 2, 5, 6, 4],
#  [6, 6, 7,6, 7, 5]]
# Will return : [(2, 2), (3, 4), (2, 4)]


def find_spectators(matrix_of_heights):
    seats = []

    number_of_rows = len(matrix_of_heights)
    number_of_columns = len(matrix_of_heights[0])

    for row in range(number_of_rows):
        for column in range(number_of_columns):
            height = matrix_of_heights[row][column]

            for front_row in range(row):
                if matrix_of_heights[front_row][column] >= height:
                    seats.append((row, column))
                    break

    return seats


print("-----Ex 9-----")
heights = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]]

seats_with_problems = find_spectators(heights)
print("Seats where spectator can't see:", seats_with_problems)


# 10. Write a function that receives a variable number of lists and returns a list of tuples as follows: the first
# tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists,
# etc. Example: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. Note: If
# input lists do not have the same number of items, missing items will be replaced with None to be able to generate
# max ([len(x) for x in input_lists]) tuples.


def create_lists(*lists):
    max_length = max(len(lista) for lista in lists)

    list_of_tuples = []
    for i in range(max_length):
        items = [lista[i] if i < len(lista) else None for lista in lists]
        list_of_tuples.append(tuple(items))

    return list_of_tuples


print("-----Ex 10-----")
print("List of tuples:", create_lists([1, 2, 3, 4], [5, 6, 7], ["a", "b", "c"]))


# 11.Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the
# tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]


def sorting_function(item):
    second_element = item[1]
    return second_element[2] if len(second_element) > 2 else None


def sort_tuples(list_of_tuples):
    sorted_tuples = sorted(list_of_tuples, key=sorting_function)
    return sorted_tuples


print("-----Ex 11-----")
print("Sorted tuples:", sort_tuples([('abc', 'bcd'), ('abc', 'zza')]))

# 12.Write a function that will receive a list of words as parameter and will return a list of lists of words,
# grouped by rhyme. Two words rhyme if both of them end with the same 2 letters. Example: group_by_rhyme(['ana',
# 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]


def group_by_rhyme(list_of_words):
    dict_of_rhymes = {}

    for word in list_of_words:
        rhyme = word[-2:] if len(word) >= 2 else word

        if rhyme in dict_of_rhymes:
            dict_of_rhymes[rhyme].append(word)
        else:
            dict_of_rhymes[rhyme] = [word]

    grouped = list(dict_of_rhymes.values())

    return grouped


print("-----Ex 12-----")
print("Grouped by rhymes:", group_by_rhyme(['ana','banana', 'a', 'ab', 'aab', 'carte', 'arme', 'parte']))




