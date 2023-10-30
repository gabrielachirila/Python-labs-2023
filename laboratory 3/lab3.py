# 1.Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a
# intersected with b, a reunited with b, a - b, b - a)

def sets_operations(a, b):
    a = set(a)
    b = set(b)

    intersection = a & b
    # or
    # intersection = a.intersection(b)

    reunion = a | b
    # or
    # reunion = a.union(b)

    a_minus_b = a - b
    # or
    # a_minus_b = a.difference(b)

    b_minus_a = b - a

    return intersection, reunion, a_minus_b, b_minus_a


print("-----Ex 1-----")

a = [0, 1, 2, 2, 3]
b = [0, 2, 4, 5]
result = sets_operations(a, b)

print("First list: {} \nSecond list: {}".format(a, b))
print("Intersection: {} \nReunion: {} \na - b: {} \nb - a: {}".format(result[0], result[1], result[2], result[3]))


# 2.
# Write a function that receives a string as a parameter and returns a dictionary in which the keys are the
# characters in the character string and the values are the number of occurrences of that character in the given
# text. Example: For string "Ana has apples." given as a parameter the function will return the dictionary:
# {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .


def character_occurrence(text):
    result = dict.fromkeys(text, 0)
    for character in text:
        result[character] += 1
    return result


print("-----Ex 2-----")
text = "Ana has apples."
ex_2 = character_occurrence(text)
print("The dictionary for characters in - {} -  is: {}".format(text, ex_2))

# 3.
# Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must
# be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)


def compare_dictionaries(dict1, dict2):
    if type(dict1) != type(dict2):
        return False

    if isinstance(dict1, dict):
        for key in dict1:
            if key not in dict2:
                return False
        for key in dict2:
            if key not in dict1:
                return False
        for key in dict1:
            if not compare_dictionaries(dict1[key], dict2[key]):
                return False

    elif isinstance(dict1, list):
        if len(dict1) != len(dict2):
            return False
        for i in range(len(dict1)):
            if not compare_dictionaries(dict1[i], dict2[i]):
                return False

    elif dict1 != dict2:
        return False

    return True


print("-----Ex 3-----")
dict1 = {
    "nume": "Sephora",
    "adresa": {
        "strada": "Victoriei",
        "oras": "Iasi"
    },
    "varsta": 30
}

dict2 = {
    "nume": "Olivia",
    "varsta": 21,
    "adresa": {
        "strada": "Independentei",
        "oras": "Bucuresti"
    }
}

dict3 = {
    "nume": "Elena",
    "varsta": 45
}

dict4 = {
    "nume": "Sephora",
    "varsta": 30,
    "adresa": {
        "strada": "Victoriei",
        "oras": "Iasi"
    }
}

result1 = compare_dictionaries(dict1, dict2)
result2 = compare_dictionaries(dict1, dict3)
result3 = compare_dictionaries(dict1, dict4)

print("Are dict1 and dict2 equal?", result1)
print("Are dict1 and dict3 equal?", result2)
print("Are dict1 and dict4 equal?", result3)

# 4.
# The build_xml_element function receives the following parameters: tag, content, and key-value elements given as
# name-parameters. Build and return a string that represents the corresponding XML element. Example:
# build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns
# the string =
# <a href="http://python.org" _class="my-link" id="someid"> Hello there </a>

# Operator ** can be used in a function to specify that the list of parameters of that
# function should be treated as a dictionary.


def build_xml_element(tag, content, **element):
    result = "<" + tag + " "

    for key, value in element.items():
        value = value.strip()
        # The default behavior of the strip() method is to remove the whitespace from the beginning and
        # at the end of the string.
        result += key + '="' + value + '"' + " "

    result += "> " + content + " </" + tag + ">"
    return result


print("-----Ex 4-----")
result = build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid ")
print(result)


# 5.
# The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for
# a dictionary that has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix",
# "middle", "suffix"). A value is considered valid if it starts with "prefix", "middle" is inside the value (not at
# the beginning or end) and ends with "suffix". The function will return True if the given dictionary matches all the
# rules, False otherwise.
# Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"} => False because although the rules
# are respected for "key1" and "key2" "key3" that does not appear in the rules.


def validate_dict(rules, dictionary):
    for x in dictionary:
        rules_x = {r for r in rules if r[0] == x}
        if len(rules_x) == 0:
            return False
        for rule in rules_x:
            key, prefix, middle, suffix = rule
            value = dictionary[x]
            value = value.strip()
            if prefix != "" and not value.startswith(prefix):
                return False
            if suffix != "" and not value.endswith(suffix):
                return False
            if middle != "" and middle not in value[1:-1]:
                return False
    return True


print("-----Ex 5-----")
result1 = validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                       {"key1": "come inside, it's too cold out", "key3": "this is not valid"})
result2 = validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                       {"key1": "come inside, it's too cold out", "key2": "start middle in winter"})
result3 = validate_dict({("key1", "", "inside", ""), ("key2", "winter", "middle", "winter")},
                       {"key1": "come inside, it's too cold out", "key2": "winter middle in winter"})
print("For the first example: {} ".format(result1))
print("For the second example: {} ".format(result2))
print("For the third example: {} ".format(result3))

# 6.
# Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of
# unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve
# this objective).


def count_unique_duplicate_elements(elements):
    set_elements = set(elements)
    count_unique = 0
    count_duplicate = 0

    for element in set_elements:
        if elements.count(element) == 1:
            count_unique += 1
        else:
            count_duplicate += 1

    return count_unique, count_duplicate


print("-----Ex 6-----")
list_of_elements = [5, 5, 5, 3, 2, 2, 1, 4]
result = count_unique_duplicate_elements(list_of_elements)
print("Given this list: {} \nNumber of unique elements: {} \nNumber of duplicate elements: {}".format(
    list_of_elements, result[0], result[1]))

# 7.
# Write a function that receives a variable number of sets and returns a dictionary with the following operations
# from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b",
# where a and b are two sets, and op is the applied operator: |, &, -.
# Ex: {1,2}, {2, 3} =>
# {
#     "{1, 2} | {2, 3}":  {1, 2, 3},
#     "{1, 2} & {2, 3}":  { 2 },
#     "{1, 2} - {2, 3}":  { 1 },
#     ...
# }


def set_operations_dictionary(*sets):
    results = {}

    for i in range(len(sets)-1):
        for j in range(i + 1, len(sets)):
            a = sets[i]
            b = sets[j]
            results["{} | {}".format(a, b)] = a | b
            results["{} & {}".format(a, b)] = a & b
            results["{} - {}".format(a, b)] = a - b
            results["{} - {}".format(b, a)] = b - a

    return results


print("-----Ex 7-----")
set1 = {1, 2}
set2 = {2, 3}
set3 = {3, 4}
print("set1: {} \nset2: {} \nset3: {}".format(set1, set2, set3))
result = set_operations_dictionary(set1, set2, set3)
for key, value in result.items():
    print("{}: {}".format(key, value))

# 8.
# Write a function that receives a single dict parameter named mapping. This dictionary always contains a string
# key "start". Starting with the value of this key you must obtain a list of objects by iterating over mapping in the
# following way: the value of the current key is the key for the next value, until you find a loop (a key that was
# visited before). The function must return the list of objects obtained as previously described.

# Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) will return [
# 'a', '6', 'z', '2']


def loop(mapping):
    current_key = "start"
    visited = set()
    result = []

    while current_key in mapping and current_key not in visited:
        visited.add(current_key)
        result.append(mapping[current_key])
        current_key = mapping[current_key]

    return result


print("-----Ex 8-----")
x = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result = loop(x)
print("Given this: {}, \nThe result is: {}".format(x,result))

# 9.
# Write a function that receives a variable number of positional arguments and a variable number of keyword
# arguments adn will return the number of positional arguments whose values can be found among keyword arguments
# values. Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return 3


def my_function(*positional_arguments, **keyword_arguments):
    keyword_values = keyword_arguments.values()
    count = 0

    for argument in positional_arguments:
        if argument in keyword_values:
            count += 1

    return count


print("-----Ex 9-----")
result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print("{} -> positional arguments that can be found among keyword arguments".format(result))
