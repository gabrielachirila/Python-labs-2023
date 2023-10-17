# Ex1
# Find The greatest common divisor of multiple numbers read from the console.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def ex_1():
    print("Ex 1")
    x = list(map(int, input("Enter numbers for which to calculate The Greatest Common Divisor: ").split()))
    # print("List of numbers: ", x)

    result = x[0]

    for num in x[1:]:
        result = gcd(num, result)

    print("The greatest common divisor is:", result)


ex_1()

# Ex2
# Write a script that calculates how many vowels are in a string.


def ex_2():
    print("Ex 2")
    # input_string = "abababEbo"
    input_string = input("Enter the text for calculating the vowels: ")
    count = 0

    for i in input_string:
        if i in "aeiouAEIOU":
            count = count + 1

    print("Vowels number:", count)


ex_2()

# Ex 3
# Write a script that receives two strings and prints the number of occurrences of the first string in the second.

def ex_3():
    print("Ex 3")
    substring = input("Enter the first string: ")
    entire_string = input("Enter the second string: ")

    occurrences = 0

    if len(substring) < len(entire_string):
        for idx, i in enumerate(entire_string):
            if len(substring) <= len(entire_string)-idx:
                if entire_string[idx] == substring[0]:
                    j = 1
                    ok = 1
                    while j < len(substring)-1:
                        if substring[j] != entire_string[idx+j]:
                            ok = 0
                            break
                        j += 1
                    if ok == 1:
                        # print(i)
                        # print(idx)
                        occurrences += 1
        print("Number of occurrences of the first string in the second string:", occurrences)
    else:
        print("The first string should be shorter than the second")

ex_3()

# Ex 4
# Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.


def ex_4():
    print("Ex 4")
    input_string = input("Enter the string in UpperCamelCase: ")

    result = [input_string[0].lower()]

    for char in input_string[1:]:
        if char.isupper():
            result.append('_')
        result.append(char.lower())

    # The join() method takes all items in an iterable and joins them into one string.
    print(''.join(result))


ex_4()

# Ex 5
# Given a square matrix of characters write a script that prints the string obtained
# by going through the matrix in spiral order (as in the example):


def ex_5():
    print("Ex 5")
    matrix = [
        ["f", "i", "r", "s"],
        ["n", "_", "l", "t"],
        ["o", "b", "a", "_"],
        ["h", "t", "y", "p"]
    ]

    result_string = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # top
        for i in range(left, right + 1):
            result_string.append(matrix[top][i])
        top += 1

        # right
        for i in range(top, bottom + 1):
            result_string.append(matrix[i][right])
        right -= 1

        # bottom
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result_string.append(matrix[bottom][i])
            bottom -= 1

        # left
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result_string.append(matrix[i][left])
            left += 1

    print(''.join(result_string))


ex_5()

# Ex 6
# Write a function that validates if a number is a palindrome.


def ex_6():
    print("Ex 6")
    number = int(input("Introduce a number to see if it's palindrome or not: "))

    aux_number = number
    reversed_number = 0

    while aux_number > 0:
        reversed_number = reversed_number * 10 + aux_number % 10
        aux_number //= 10

    # print("reversed:", reversed_number)

    if number == reversed_number:
        print(number, "is palindrome")
    else:
        print(number, "is NOT palindrome")


ex_6()

# Ex 7
# Write a function that extract a number from a text
# (for example if the text is "An apple is 123 USD", this function will return 123,
# or if the text is "abc123abc" the function will extract 123).
# The function will extract only the first number that is found.


def ex_7():
    print("Ex 7")
    input_string = input("Introduce a text: ")
    number_str = ""
    found_number = False

    for char in input_string:
        if char.isdigit():
            number_str += char
            found_number = True
        elif found_number:
            break

    if number_str:
        print(int(number_str))
    else:
        print("Number was not found")


ex_7()


# Ex 8
# Write a function that counts how many bits with value 1 a number has.
# For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"

def ex_8():
    print("Ex 8")
    number_input = int(input("Introduce a number: "))

    binary_representation = bin(number_input)
    count = binary_representation.count('1')

    print(f"{count} bits with value 1 in number {number_input}")


ex_8()

# Ex 9
# Write a functions that determine the most common letter in a string.
# For example if the string is "an apple is not a tomato",
# then the most common character is "a" (4 times).
# Only letters (A-Z or a-z) are to be considered.
# Casing should not be considered "A" and "a" represent the same character.


def ex_9():
    print("Ex 9")
    input_string = input("Introduce a text: ")

    letter_count = {}

    for char in input_string:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    if letter_count:
        most_common = max(letter_count, key=letter_count.get)
        print(f"most common character is: {most_common}, {letter_count[most_common]} times")
    else:
        print("Not found")


ex_9()

# Ex 10
# Write a function that counts how many words exists in a text.
# A text is considered to be form out of words that are separated by only ONE space.
# For example: "I have Python exam" has 4 words.


def ex_10():
    print("Ex 10")
    input_string = input("Introduce a text: ")
    words = input_string.split(" ")
    word_count = len(words)
    print(f"The text contains {word_count} words.")


ex_10()
