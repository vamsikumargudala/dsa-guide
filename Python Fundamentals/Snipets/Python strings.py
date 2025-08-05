# Looping Through Python Strings and Mastering Character Operations:

# Strings are a collection of characters enclosed within single, double, or triple quotes. They are immutable, meaning you cannot change the characters in a string after it is created.

# Strings are enclosed by either single, double, or triple quotes. Here are a few examples:

greeting = 'Hello, World!'
greeting_double = "Hello, World!"
greeting_triple = """Hello, World!"""

# Accessing elements in a string
first_char = greeting[0]
last_char = greeting[-1]

#  looping concepts in Python, with a specific focus on strings. We will explore how to iterate over strings, access individual characters, and perform common operations like slicing and concatenation.

# String Indexing Reminder
# Strings are indexed in Python, meaning each character in the string has a unique position or index. We can access individual characters by their index using square brackets [].

# Indexing starts from 0, with the first character at index 0, the second character at index 1, and so on. We can also use negative indexing, where -1 denotes the last character, -2 denotes the second last character, and so on.

try:
    text: str = 'Hello, World!'
    print(text[0])  # Outputs: H
    print(text[-1])  # Outputs: !
except IndexError as e:
    print("character not found")

# This code will output the first and last characters of the string text. The first character 'H' is accessed using the index 0, while the last character '!' is accessed using the index -1. The try-except block helps us handle any IndexError, which can transpire when we attempt to access an index that doesn't exist in our string.

# Character Operations
#  Python provides various built-in functions, such as ord(), chr(), upper(), lower(), and isalpha(). We'll consider how such functions can prove advantageous in real-world scenarios, like data cleaning, where one might need to standardize the case of the text data.


# The ord() and chr() functions could prove valuable when implementing encryption algorithms. Specifically, ord(c) returns an ASCII ordinal number of the provided character c, and chr(c) converts the provided ASCII ordinal number back to the character. Have a look at the example:

char = 'A'
ascii_value = ord(char)
print(ascii_value)  # Outputs: 65

char = chr(ascii_value)
print(char)  # Outputs: A

print(ascii_value+1)  # Outputs: 66
print(char(ascii_value+1))  # Outputs: B

# The upper() and lower() functions are used to convert the text to uppercase and lowercase, respectively. These functions are beneficial when you need to standardize the case of the text data.

text = 'Hello, World!'
upper_text = text.upper() # Outputs: HELLO, WORLD!
lower_text = text.lower() # Outputs: hello, world!

# The isalpha(), isdigit(), and isalnum() methods are useful when you need to check whether the character or all letters in the string satisfy a specific condition (are all letters, all digits, or letters/digits, respectively).

text = 'Vamsi123'
is_alpha = text.isalpha() # Outputs: False
is_digit = text.isdigit() # Outputs: False
is_alnum = text.isalnum() # Outputs: True

print("C".isalpha()) # Prints: True
print("C++".isalpha()) # Prints: False
print("239".isdigit()) # Prints: True
print("C239".isdigit()) # Prints: False
print("C98".isalnum()) # Prints: True
print("C98++".isalnum()) # Prints: False

# Python String Methods and Type Conversions

# Python provides a wide range of built-in string methods that can be used to manipulate and transform strings. These methods are useful for various tasks, such as searching for substrings, replacing text, and formatting strings.we'll Explore pthon's string methods: split(), join(), strip(), and learn how to perform type conversions. Python's robust built-in string methods simplify text processing, enhancing the readability and efficiency of our code.


# The split() method is used to split a string into a list of substrings based on a specified delimiter. This method is particularly useful when you need to extract individual words or tokens from a sentence.

sentence = 'hello world this is a sentence'
words = sentence.split() # # no delimiter provided, splitting by whitespace
print(words)  # Outputs: ['hello', 'world', 'this', 'is', 'a', 'sentence']

#  we observe that split() divides sentence into words. We can also opt for different delimiters, such as a comma.
fruits = 'apple,banana,cherry'
fruit_list = fruits.split(',')
print(fruit_list)  # Outputs: ['apple', 'banana', 'cherry']

# The join() method is used to concatenate a list of strings into a single string. This method is the inverse of the split() method and is particularly useful when you need to combine multiple strings into a single string.

words = ['hello', 'world', 'this', 'is', 'a', 'sentence']
sentence = ' '.join(words)
print(sentence)  # Outputs: hello world this is a sentence

# The strip() method is used to remove leading and trailing whitespace characters from a string. This method is beneficial when you need to clean up text data by removing unnecessary spaces.

text = '   hello, world!   '
clean_text = text.strip()
print(clean_text)  # Outputs: hello, world!

# further more, we can also remove specific characters from the beginning and end of a string using the strip() method. For example, to remove commas and exclamation marks from the beginning and end of a string, we can use the following code:

print('hello, world!'.strip(',!'))  # Outputs: hello, world

name = '   vamsikumar   '
print(name.lstrip())  # Outputs: 'vamsikumar  '
print(name.rstrip())  # Outputs: '  vamsikumar'

# Type Conversions
# Python provides built-in functions to convert between different data types. These functions are particularly useful when you need to convert strings to numbers or vice versa.
num_str = '123'
print(type(num_str))  # Outputs: <class 'str'>
num = int(num_str)
print(type(num))  # Outputs: <class 'int'>

name = 'John'
age = 25
print('My name is ' + name + ', and I am ' + str(age) + ' years old.')
# Prints: My name is John, and I am 25 years old.

# Combining split(), join(), strip(), and Type Conversions Together
# We can combine the split(), join(), strip(), and type conversion functions to perform complex text processing tasks. For example, we can extract numbers from a string, perform calculations, and convert the results back to a string for display.

# Extracting numbers from a string
text = 'The price of the product is $25.50'
price_str = text.split('$')[1].strip()
price = float(price_str)
tax = 0.1 * price
total = price + tax

result_text = f'The total price including tax is ${total:.2f}'
# Prints: The total price including tax is $28.05