[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21943637)

# Loops Assignment — `while` and `for`

In this assignment you will practice **`while` loops** and **`for` loops** in Python, sometimes combined with lists and dictionaries.

You should already have seen loops in the lecture.
This assignment is designed to:

* refresh the basic syntax
* train you to think in terms of **repetition** and **accumulation**
* prepare you for more complex problems that use loops later

You will work with:

* **`while` loops** → repeat *until* some condition is met
* **`for` loops** → repeat a fixed number of times or over items in a sequence
* **lists** → store multiple values
* **dictionaries** → store key–value pairs

---

## 📚 Useful References (W3Schools)

* `while` loops: [https://www.w3schools.com/python/python_while_loops.asp](https://www.w3schools.com/python/python_while_loops.asp)
* `for` loops: [https://www.w3schools.com/python/python_for_loops.asp](https://www.w3schools.com/python/python_for_loops.asp)

If you get stuck on the looping structure itself, check these pages first.

---

## 🏠 Homework Exercise 1 — `while` Loop: Sum Until Target

> **Task:**
> Ask the user for a **target number**.
> Then, using a **while loop**, repeatedly ask the user for numbers and add them to a running total.
> Stop when the total **reaches or exceeds** the target, and print the final total.

### Example interaction

```text
Target: 20
Number: 5
Number: 7
Number: 4
Number: 10
Total reached: 26
```

### Relevant concepts

* `while` loop: [https://www.w3schools.com/python/python_while_loops.asp](https://www.w3schools.com/python/python_while_loops.asp)
* Basic arithmetic and comparison: `+`, `>=`

### How to think about the solution (step by step, no code)

1. **Ask for the target once**

   * You need a value that represents the goal (for example, 20).
   * Read it from the user and convert it to an integer.

2. **Initialize a running total**

   * Create a variable, e.g. `total`, and set it to 0.
   * This variable will accumulate all the numbers the user enters.

3. **Define the loop condition**

   * You want to keep asking for numbers **while `total` is less than the target**.
   * So your loop condition should be something like: “continue as long as the total is below the target.”

4. **Inside the loop: ask for a number and update the total**

   * Each time through the loop:

     * ask the user for a number
     * convert it to an integer
     * add it to `total`.

5. **Check the condition again automatically**

   * After each iteration, Python re-checks the `while` condition.
   * If `total` is still smaller than the target → loop continues.
   * If `total` has reached or passed the target → loop stops.

6. **After the loop ends: print the total**

   * When the loop finishes, print a message with the final total, like:
     `"Total reached: 26"`.

The key idea: you are **repeating input** and **accumulating** until you hit a limit.

---

## 🏠 Homework Exercise 2 — `for` Loop: Largest of N Numbers

> **Task:**
> Write a program that first asks the user **how many numbers** they will enter.
> Then, using a **for loop**, read that many integers from the user, and at the end print out the **largest** number entered.

### Example interaction

```text
How many numbers? 4
Number 1: 10
Number 2: 5
Number 3: 27
Number 4: 12
The largest number was: 27
```

### Relevant concepts

* `for` loops: [https://www.w3schools.com/python/python_for_loops.asp](https://www.w3schools.com/python/python_for_loops.asp)

### How to think about the solution (step by step, no code)

1. **Ask how many numbers you will read**

   * Read an integer `count` that tells you how many inputs to expect.
   * This will decide how many times your `for` loop runs.

2. **Plan the `for` loop**

   * You want to repeat the same action `count` times: ask for a number and compare it.
   * Use a `for` loop with a range that runs exactly `count` iterations.

3. **Keep track of the current maximum**

   * Before the loop starts, decide how you will store the largest number so far.
   * Usually, you initialize a variable, like `max_value`.
   * You can:

     * either initialize it using the first number entered, or
     * start with something like `None` or a very small value and update it properly.

4. **Inside the loop: read the next number**

   * For each iteration:

     * print something like `"Number 1:"`, `"Number 2:"`, etc., using the loop index + 1
     * read the integer value
     * compare it with the current maximum.

5. **Update the maximum when needed**

   * If the new number is bigger than the current `max_value`, you replace `max_value` with this new number.
   * This way, after reading all numbers, `max_value` is the largest one seen.

6. **After the loop ends: print the result**

   * Print a final message such as:
     `"The largest number was: 27"`.

The key idea: you **loop a fixed number of times**, and **carry a “best so far” value** that you update whenever you see something larger.

---

## 🏫 In-class Exercise 3 — `while` Loop: PIN Code Attempts

> **Task:**
> Write a program that keeps asking the user for a PIN code until they type `4321`.
> For each incorrect attempt, print `"Wrong"`.
> When they finally enter `4321`, print how many attempts it took.

### Example interaction 1

```text
PIN: 3245
Wrong
PIN: 1234
Wrong
PIN: 0000
Wrong
PIN: 4321
Correct! It took you 4 attempts
```

### Example interaction 2 (first try correct)

```text
PIN: 4321
Correct! It only took you one single attempt!
```

### Relevant concepts

* `while` loop with a condition that depends on user input
* counting attempts
* simple `if` for special message (single attempt vs. multiple attempts)

**Strategy to solve:**

* Keep a counter of attempts.
* Use a `while` loop that continues while the entered PIN is not `4321`.
* After each wrong input, print `"Wrong"` and increment the counter.
* When the user gets it right, print a different message depending on whether the counter is 1 or more.

---

## 🏫 In-class Exercise 4 — `for` Loop: Print All Numbers Below Input

> **Task:**
> Ask the user for a positive integer `n`.
> Using a **for loop**, print all positive integers greater than 0 and **smaller** than `n`.

### Example

```text
Upper limit: 5
1
2
3
4
```

### Relevant concepts

* `for` loop over a `range()`
* `range(start, end)` includes `start` but excludes `end`.

**Strategy to solve:**

* Ask for `n` and convert it to an integer.
* Use a `for` loop with `range(1, n)` (this starts at 1 and goes up to `n-1`).
* Print the loop variable on each iteration.

---

## ⭐ Optional Exercise 5 — `for` Loop + List Processing

> **Task:**
> You are given the following list:
>
> ```python
> numbers = [3, 8, 12, 7, 9, 10, 21, 30]
> ```
>
> Using a **for loop**, go through the list, find all **even** numbers, and:
>
> * count how many even numbers there are
> * build a **new list** containing only the even numbers
> * print the list of even numbers and the total count

### Example output

```text
Even numbers: [8, 12, 10, 30]
Total: 4
```

### Relevant concepts

* `for` over a list: [https://www.w3schools.com/python/python_for_loops.asp](https://www.w3schools.com/python/python_for_loops.asp)
* `%` operator to check even/odd

**Strategy to solve:**

* Start with an empty list for evens and a counter set to 0.
* Loop over each item in `numbers`.
* If the number is even:

  * append it to the new list
  * increase the counter by 1
* After the loop, print the list and the count.

---

## ⭐ Optional Exercise 6 — `while` Loop + Dictionary Lookup

> **Task:**
> You are given this dictionary:
>
> ```python
> translations = {
>     "cat": "pisică",
>     "dog": "câine",
>     "red": "roșu",
>     "sun": "soare"
> }
> ```
>
> Using a **while loop**, repeatedly ask the user for an English word:
>
> * if the user types `"exit"`, stop the loop and print a goodbye message
> * if the word exists in the dictionary, print the Romanian translation
> * otherwise, print `"Word not found"`

### Example interaction

```text
Word: cat
pisică
Word: tree
Word not found
Word: dog
câine
Word: exit
Goodbye!
```

### Relevant concepts

* `while` for repeated input: [https://www.w3schools.com/python/python_while_loops.asp](https://www.w3schools.com/python/python_while_loops.asp)
* dictionary key lookup: [https://www.w3schools.com/python/python_dictionaries.asp](https://www.w3schools.com/python/python_dictionaries.asp)

**Strategy to solve:**

1. Keep the `translations` dictionary defined at the top.
2. Start an infinite-like `while` loop that breaks only when `"exit"` is entered.
3. Each time:

   * ask for a word
   * if it’s `"exit"`, break the loop (and print a goodbye message)
   * else, check if the word exists as a key in the dictionary
   * if it does, print the value (translation)
   * otherwise, print `"Word not found"`.

The key idea here is combining a **loop that doesn’t know in advance how many times it will run** with **dictionary lookups**.

---
