import random

# INSTRUCTIONS

# In case it is not clear, the Question appears first, then examples, then any hints and finally the function that you need to complete appears underneath:

# <QUESTION>

# <EXAMPLES>

# <HINT>

# You are NOT allowed access to the internet for this assessment, instead you should use the DOCUMENTATION that comes bundled with your Python installation.  You should already be comfortable accessing this documentation, but to summarise:

# Access Python from you CLI

# Type help() or for example help(str)


# <QUESTION 1>

# Given a string, return a string where for every char in the original string, there are three chars.

# <EXAMPLES>

# one("The") → "TTThhheee"
# one("AAbb") → "AAAAAAbbbbbb"
# one("Hi-There") → "HHHiii---TTThhheeerrreee"

# <HINT>
# How does a for loop iterate through a string?


def one(string):
    word = ''
    for i in range (len(string)):
        word = word + string[i] + string[i] + string[i]
        return word
    

    # <QUESTION 2>

    #  Write a function which returns the boolean True if the input is only divisible by one and itself.

    # The function should return the boolean False if not.

    # <EXAMPLES>

    # two(3) → True
    # two(8) → False

    # <HINT>
    # What operator will give you the remainder?
    # Use your CLI to access the Python documentation and get help manipulating strings - help(range).


def two(num):
     for i in range (2, num):
        if num % i == 0:
            return False
        else:
            return True
    
print(two(5))
    # <QUESTION 3>

    # Write a function which takes an integer input, a, and returns the sum a+aa+aaa+aaaa.

    # So if 2 was the input, the function should return 2+22+222+2222 which is 2468.

    # <EXAMPLES>

    # three(9) → 11106
    # three(5) → 6170

    # <HINT>
    # What happens if you multiply a string by a number?


def three(a):
    a_list = []
    b = str()
    for i in range(4):
        b += str(a)
        a_list.append(int(b))
    return sum(a_list)
    

    # <QUESTION 4>

    # Given two Strings of equal length, 'merge' them into one String.

    # Do this by 'zipping' the Strings together.

    # Start with the first char of the first String.
    # Then add the first char from the second String.
    # Then add the second char from the first String.
    # And so on.

    # Maintain case.

    # You will not encounter whitespace.

    # <EXAMPLES>

    # four("String","Fridge") → "SFtrriidngge"
    # four("Dog","Cat") → "DCoagt"
    # four("True","Tree") → "TTrrueee"
    # four("return","letter") → "rleettutrenr"

    # <HINT>
    # Use your CLI to access the Python documentation and get help manipulating strings - help(list.insert).
    # How would you seperate a string into characters?


def four(string1, string2):
    phrase = ""
    for i in range (len(string1)):
        phrase = phrase + string1[i] + string2[i]
    return phrase
    

    # <QUESTION 5>

    # Write a function to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

    # <EXAMPLES>

    # five() → [100,102,122,198,200]
    # five() → [108,104,106,188,200]
    # five() → [154,102,132,178,164]

    # <HINT>
    # There is a module which can be used to generate random numbers, this module is called random.
    # The random module contains a function called randint.


def five():
    return(random.sample([i for i in range(100,201) if i%2==0], 5))

print(five())

def five1():
    numlist = []
    for i in range (100, 201):
        if i % 2 == 0:
            numlist = numlist + [i]

    return random.sample(list(numlist), 5)

print (five1())

    # <QUESTION 6>

    # Given a string, return the boolean True if it ends in "py", and False if not.

    # Ignore Case.

    # For Example:

    # six("ilovepy") → True
    # six("welovepy") → True
    # six("welovepyforreal") → False
    # six("pyiscool") → False

    # <HINT>
    # There are no hints for this question.


def six(string):
    word = string.casefold()
	if word.endswith('py'):
		return True
    else:
	    return False
    

    # <QUESTION 7>

    # Given three ints, a b c, one of them is small, one is medium and one is large.

    # Return the boolean True if the three values are evenly spaced, so the
    # difference between small and medium is the same as the difference between
    # medium and large.

    # Do not assume the ints will come to you in a reasonable order.

    # <EXAMPLES>

    # seven(2, 4, 6) → True
    # seven(4, 6, 2) → True
    # seven(4, 6, 3) → False
    # seven(4, 60, 9) → False

    # <HINT>
    # There is a function for lists called sort.
    # Use the cli to access the documentation help(list.sort)


def seven(a, b, c):
    num = [a, b, c]
    num.sort()
    if (num[1] - num[0]) == (num[2] - num[1]):
        return True
    return False

    # <QUESTION 8>

    # Given a string and an integer, n, return a string that removes n letters from the 'middle' of the string.

    # The string length will be at least n, and be odd when the length of the input is odd, so there will always be a 'middle'.

    # <EXAMPLES>

    # eight("Hello", 3) → "Ho"
    # eight("Chocolate", 3) → "Choate"
    # eight("Chocolate", 1) → "Choclate"

    # <HINT>
    # Use the cli to access the documentation help(str.replace)


def eight(string, num):
    word = string
	for i in range(num):
		middle = len(word)//2
		word = word[:middle] + word[(middle + 1):]
	return word
    

    # <QUESTION 9>

    # Given two string inputs, if one can be made from the other return the boolean True, if not return the boolean False.

    # <EXAMPLES>

    # nine("god", "dog") → True
    # nine("tree", "tiredest") → True
    # nine("cat", "dog") → False
    # nine("tripping", "gin") → True

    # <HINT>
    # There are no hints for this question.


def nine(string1, string2):
    # make sure string1 is the shortest of the two
     s1 = 0
    sorted_string1 = sorted(string1.lower())
    sorted_string2 = sorted(string2.lower())

    for char in sorted_string2:
        if char in sorted_string1:
            s1 += 1
    if s1 >= len(string1) or s1 >= len(string2):
        return True
    else:
        return False

    # <QUESTION 10>

    # Write a function which takes 2 integers greater than 0, X,Y as input and generates a 2-dimensional array.

    # The element value in the i-th row and j-th column of the array should be i*j.

    # <EXAMPLES>

    # ten(3,2) → [[0,0,0],[0,1,2]]
    # ten(2,1) → [[0,0]]
    # ten(3,4) → [[0,0,0],[0,1,2],[0,2,4],[0,3,6]]

    # <HINT>
    # Think about nesting for loops.


def ten(a, b):
    array = [[0 for aa in range(a)] for bb in range(b)]
	for bb in range(b):
		for aa in range(a):
			array[bb][aa] = aa * bb
	return array
    