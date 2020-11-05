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
