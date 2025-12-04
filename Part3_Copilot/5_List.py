# https://www.w3schools.com/python/python_for_loops.asp
#
# You are given the following list:
# numbers = [3, 8, 12, 7, 9, 10, 21, 30]
#
# Write a program that:
#   - uses a for loop to go through the list
#   - counts how many numbers are even
#   - creates a new list containing only the even numbers
#   - prints the even numbers list and the total count
#
# Sample output:
# Even numbers: [8, 12, 10, 30]
# Total: 4
#
# Requirements:
#   - must use a for loop
#   - no list comprehensions
#   - simple logic only

# Write your code here:
numbers = [3, 8, 12, 7, 9, 10, 21, 30]

even_numbers = []
count = 0
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
        count += 1

print(f"Even numbers: {even_numbers}")
print(f"Total: {count}")

