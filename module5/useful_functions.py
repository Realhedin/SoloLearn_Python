# string functions
def string_functions_print():
    # join list of strings using separator 'kkk'
    str1 = 'ab'
    str2 = 'bc'
    str3 = 'cd'
    separator = 'kkk'
    strJoined = separator.join([str1, str2, str3])
    print(strJoined)
    # replace
    print("Hello ME".replace("ME", "world"))
    # startWith
    print("This is a sentence.".startswith("This"))
    # endWith
    print("This is a sentence.".endswith("sentence."))
    # upper
    print("This is a sentence.".upper())
    # lower
    print("AN ALL CAPS SENTENCE".lower())
    # split string into list by separator
    print("spam, eggs, ham".split(", "))


def numberic_functions_print():
    print(min(1, 2, 3, 4, 0, 2, 1))
    print(max([1, 4, 9, 2, 5, 6, 8]))
    print(abs(-99))
    print(abs(42))
    print(sum([1, 2, 3, 4, 5]))
    print(round(7.1))

def list_functions_print():
    nums = [55, 44, 33, 22, 11]
    #if requires all elements to be greater than 5
    if all([i > 5 for i in nums]):
        print("All larger than 5")
    #if requires that at least one satisfy
    if any([i % 2 == 0 for i in nums]):
        print("At least one is even")
    #iterate through list with index and values
    for idx, v in enumerate(nums):
        print(idx, v)