# https://www.w3schools.com/python/python_while_loops.asp

# Write a program that asks the user for a target number.
# Using a while loop, repeatedly ask the user for numbers and keep
# adding them to a running total.
#
# The loop should stop when the total reaches or exceeds the target.
# After the loop ends, print the final total.
#
# Sample interaction:
# Target: 20
# Number: 5
# Number: 7
# Number: 4
# Number: 10
# Total reached: 26
#
# Hints:
#   - Ask for the target once (outside the loop)
#   - Start a variable total = 0
#   - In each iteration, ask for a new number and add it to total
#   - Stop only when total >= target

# Write your code here:

target = int(input("Type in a target number : "))

total = 0
while total < target:
    number = int(input("Type in a number : "))
    total += number 

    