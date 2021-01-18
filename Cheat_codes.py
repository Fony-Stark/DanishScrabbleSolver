import itertools

val = input("input your letters as: abcd - ")

points = {"a": 1, "b": 3, "c": 8, "d": 2, "e": 1, "f": 3, "g": 3, "h": 4, "i": 3,
          "j": 4, "k": 3, "l":2, "m":4, "n":1, "o":2, "p":4, "q":4, "r":1, "s":2,
          "t":2, "u":3, "v":4, "w":4, "x":8, "y":4, "z":9, "æ":4, "ø":4, "å":4}

print("This is the values, with it is calculated with: ", points)
print("This is your letters:", val)

def bruteforce(string, solution):
    S = list(string)
    for i in range(len(S)+1):
      for c in itertools.combinations(S, i):
        cc = ''.join(c)
        if(check_for_word(cc)):
            solution[cc] = calc_value(cc)

def check_for_word(string):
    s = string + "\n"
    read_file = open("fixed_danske_ord.txt", "r")
    Lines = read_file.readlines()
    for line in Lines:
        if(line == s):
            read_file.close()
            return True
    read_file.close()
    return False

def calc_value(string):
    value = 0
    for letter in string:
        value += points[letter]

    return value

sol = {}
bruteforce(val, sol)
print("This is what you can do:", sol)
