def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


def read_file_and_count_characters(filename, char):
    with open(filename) as f:
        text = f.read()
    print("Num of {0} char".format(count_char(text, char)))
    alphabet_percentage_for_char(text)


def alphabet_percentage_for_char(text):
    for char in "abcdefghijklmnopqrstuvwxyz":
        perc = 100 * count_char(text, char) / len(text)
        print("{0} - {1}%".format(char, round(perc, 2)))