# Looping in Python: Understanding For and While Loops with Collections

# we will revisit Python loops, essential tools that simplify repetitive tasks. Think of loops like a marathon of TV series episodes. We will venture into the Python looping universe and acquire hands-on experience by applying loops to collections like lists and strings.

# Understanding Looping

friends = ['Alice', 'Bob', 'Charlie', 'David']
for friend in friends:
    print(f"Hello, {friend}! Nice to meet you.")

# The for loop iterates over each element in the list friends and prints a greeting message for each friend. The loop continues until it reaches the end of the list.

for num in range(5):
    print(num)

# The while loop is another looping construct in Python. It repeats a block of code as long as a condition is true. Let's see an example:

num = 0
while num < 5:
    print(num)
    num += 1

# Looping Over Collections
for index, friend in enumerate(friends):
    print(f"Friend {index}: {friend}")

# The enumerate function returns both the index and the element in each iteration. This is useful when you need to access both the index and the element in a loop.

# Looping Over Strings
for char in 'Hello':
    print(char)

# The for loop can iterate over each character in a string. This is useful when you need to process each character individually.

# Looping with Break and Continue
for num in range(10):
    if num == 5:
        break
    print(num)

# The break statement terminates the loop when the condition num == 5 is met. This is useful when you want to exit the loop early.

# Applications of Looping

# Let's see how we can use loops to solve a problem. Suppose we have a list of numbers and we want to find the sum of all the numbers in the list. We can use a for loop to iterate over the list and accumulate the sum.

numbers = [1, 2, 3, 4, 5]
sum = 0   # Initialize the sum to 0
for num in numbers:
    sum += num
print(f"The sum of the numbers is: {sum}")

# In this example, we use a for loop to iterate over the list numbers and accumulate the sum of all the numbers. The sum is initialized to 0 before the loop starts.

text  = 'hello'
vowel_count = 0
for char in text:
    if char in 'aeiou':
        vowel_count += 1
print(f"The number of vowels in the text is: {vowel_count}")

# Conditional Looping, Break, and Continue: Conditional Looping, along with the break and continue statements. As we know, loops enable code execution multiple times. Conditional looping, enhanced with break and continue, bolsters loop control, leading to flexible, efficient code. Grab your explorer hat, and let's get started!

# The 'If' Statement: The 'if' statement is a conditional statement that executes a block of code if a condition is true. Let's see an example:

num = 10
if num > 0:
    print("The number is positive")

temperature = 15
if temperature > 20:
    print("Wear light clothes.") # This will print if temperature is over 20.
else:
    print("Bring a jacket.") # This will print otherwise.

# The 'if' statement can be followed by an 'else' block, which executes when the condition is false. This allows you to handle both cases based on the condition.

if temperature > 30:
    print("It's hot outside!") # Prints if temperature is over 30.
elif temperature > 20:
    print("The weather is nice.") # Prints if temperature is between 21 and 30.
else:
    print("It might be cold outside.") # Prints if temperature is 20 or below.

# The 'elif' statement is short for 'else if' and allows you to check multiple conditions in sequence. The 'else' block executes when all the preceding conditions are false.

# The 'break' Statement: The 'break' statement terminates the loop when a condition is met. Let's see an example:

for num in range(10):
    if num == 5:
        break
    print(num)

# The 'continue' Statement: The continue statement bypasses the rest of the loop code for the current iteration only:
for i in range(5):
    if i == 2:
        continue
    print(i) # This will skip 2 and print the rest.

# Use-case with a For Loop
for friend in friends:
    if friend == 'Charlie':
        print("Found Charlie!")
        break
    print(f"Hello, {friend}!")


