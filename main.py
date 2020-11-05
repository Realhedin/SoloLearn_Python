# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.

def write_file_test_message(name):
    global file
    try:
        file = open(name, "w")
        file.write("test_message")
    finally:
        file.close()

def append_file_new_message(name):
    global file
    try:
        file = open(name, "a")
        file.write("this is an append message\n")
    finally:
        file.close()

def read_file(name):
    global file
    try:
        file = open(name,"r")
        readlines = file.readlines()
        for i in readlines:
            print(i)
    finally:
        file.close()

def read_file_safe_way(name):
    with open(name, "r") as f:
        readlines = f.readlines()
        for i in readlines:
            print(i)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # write_file_test_message("newFile")
    # read_file_safe_way("newFile")
    dict = {1:2, 2: "apple", 3: None}
    print(dict.get(1))
    print(dict.get(5, "test value"))
    #example list
    list = [1,2,3,4,5,6,7]
    list[1] = 5
    print(list)
    #example tuple
    tuple = (6,7,8)
    print(tuple)
    #list slicing
    print(list[3:1:-1])
    print(list[3:-1:2])
    print(list[::-1])
    #list comprehensions
    #list with i^2 from 1 until 5 (0, 1,4,9,16)
    sqs = [i**2 for i in range(5)]
    print(sqs)
    #list of i^2 from 1 until 10 but adding only even
    sqs2 = [i**2 for i in range(10) if i**2 % 2 ==0]
    print(sqs2)
    #string formatting
    print("Numbers: {x}, {y}".format(x=5,y=7))
    nums = [1,3,5]
    print("Nums: {2}, {0}, {2}".format(nums[0], nums[1], nums[2]))



