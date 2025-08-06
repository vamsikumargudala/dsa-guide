# Python collections, notably lists and strings, are fundamental to efficient programming. They allow you to handle groups of data seamlessly

# Python collections are containers that are used to store collections of data, such as lists, tuples, sets, and dictionaries. Python has several built-in data structures that help you to manage data efficiently.

# Python Collections: Gain an understanding of essential Python collections like lists and strings.
# List Operations: Learn how to create, access, and manipulate lists effectively.
# String Operations: Dive into strings and explore various operations to manage text data.
# Indexing and Slicing: Master the techniques to efficiently access and manipulate data in lists and strings.

# Simple example of a list
example_list = [1, 2, 3, 4, 5]
print(example_list[0])  # Outputs: 1

#  These collections allow Python to group multiple elements, such as numbers or characters, under a single entity. This grouping helps you to manage and manipulate data efficiently.

# We will focus mainly on Lists and Strings. A fun fact here is that Lists are mutable (we can change them after creation), while strings are immutable (unalterable post-creation). Let's see examples:

# Defining a list and a string
my_list = [1, 2, 3, 4]
my_string = 'hello'

# Now let's try to change the first element of both these collections
my_list[0] = 100
# Uncommenting the below line will throw an error
# my_string[0] = 'H'  

#They let us organize data so that each item holds a definite position or an index. The index allows us to access or modify each item individually.

fruits = ['apple', 'banana', 'cherry', 'dates', 'elderberry']

# Add a new element at the end
fruits.append('dates')

# Insert a new element at a specific index
fruits.insert(2, 'blueberry')

# Remove an element by value
fruits.remove('banana')

# Access an element by index
print(fruits[0])  # Outputs: apple
print(fruits[-1]) # Outputs: dates

# Understanding Strings
# Strings are a collection of characters enclosed within single, double, or triple quotes. They are immutable, meaning you cannot change the characters in a string after it is created.

# Strings are enclosed by either single, double, or triple quotes. Here are a few examples:

greeting = 'Hello, World!'

# Accessing elements in a string
first_char = greeting[0]
last_char = greeting[-1]

# Making it as lower 
lower_case = greeting.lower()

# Indexing and Common Operations
# Both lists and strings allow us to access individual elements through indexing. In Python, we start counting from 0, implying the first element is at index 0, the second at index 1, and so on. Negative indexing begins from the end, with -1 denoting the last element.

# We have many operations we can perform on our lists and strings. We can slice them, concatenate them, repeat them, and even find occurrence of a particular element!

slice_list = fruits[1:3]  # Outputs: ['cherry', 'dates']
slice_str = greeting[1:5]  # Outputs: 'ello'

# Concatenation: my_list + another_list
concat_list = fruits + ['gif', 'honey']
concat_str = greeting + ' Have a good day! '

# Repetition: my_list * n
repeat_list = fruits * 2 # Outputs: ['apple', 'cherry', 'dates', 'elderberry', 'apple', 'cherry', 'dates', 'elderberry']
repeat_str = greeting * 2 # Outputs: 'Hello, World!Hello, World!'

# Finding the first occurrence of an element in a list or a string
# Note that if the element is not found, `index` throws an exception
# So we should initially check the existence by the operator `in`,
# Then use the `index` method if it exists using the `if-else` construction.
# If the element is not found, the indices are assigned to `-1`.

if 'apple' in fruits:
    index = fruits.index('apple')
else:
    index = -1                                                      

