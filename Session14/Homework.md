# Python Sets -- Homework Assignment

**Level:** Beginner
**Total Questions:** 15
**Topic:** Python Sets

## Learning Objectives

By completing this homework, you should be able to:

- Explain what a Python Set is.
- Create empty and non-empty Sets.
- Understand duplicate elements and Set ordering.
- Use `add()`, `remove()`, and `pop()`.
- Explain the difference between `remove()` and `pop()`.
- Perform `union()` and `intersection()` operations.

## Instructions

1. Attempt all questions.
2. Write code wherever required.
3. Do not copy answers from notes.
4. For output questions, write the expected output.
5. Run your programs after completing the assignment.

---

## Section 1: Multiple-Choice Questions

### Q1. Which statement best describes a Python Set?

A. An ordered collection that allows duplicates
B. An unordered collection of unique elements
C. A collection of key-value pairs
D. A collection that supports indexing

### Q2. Which statement creates an empty Set?

A. `items = {}`
B. `items = []`
C. `items = set()`
D. `items = ()`

### Q3. Which method adds one element to a Set?

A. `append()`
B. `insert()`
C. `add()`
D. `push()`

### Q4. Which method removes a specified element and raises a `KeyError` if it is absent?

A. `pop()`
B. `remove()`
C. `add()`
D. `union()`

### Q5. What does `pop()` do when called on a non-empty Set?

A. Removes the smallest element
B. Removes the first inserted element
C. Removes and returns an arbitrary element
D. Removes a specified element passed as an argument

---

## Section 2: Predict the Output

### Q6. Predict the output.

```python
numbers = {2, 4, 6, 8}
numbers.add(10)

print(len(numbers))
```

**Your answer:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Q7. Predict the output.

```python
values = {5, 10, 15, 20}
values.remove(10)

print(10 in values)
```

**Your answer:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Q8. Predict the output.

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
```

**Your answer:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Q9. Predict the output.

```python
A = {10, 20, 30}
B = {20, 30, 40}

print(A.intersection(B))
```

**Your answer:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Q10. Predict the output.

```python
items = {"pen", "book", "bag"}
items.add("pen")

print(len(items))
```

**Your answer:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## Section 3: True or False

Write **True** or **False** for each statement.

### Q11.

A Python Set can contain duplicate elements.

**Your answer:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Q12.

`remove()` and `pop()` always remove the same element from a Set.

**Your answer:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Q13.

The `intersection()` method returns elements that are common to both
Sets.

**Your answer:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

---

## Section 4: Coding Questions

### Q14. Create and Update a Set

Write a Python program that:

1. Creates a Set named `subjects` containing `"Python"`, `"Java"`, and
   `"JavaScript"`.
2. Adds `"C++"` using the `add()` method.
3. Removes `"Java"` using the `remove()` method.
4. Prints the updated Set.

**Write your code below:**

```python
# Your code here
```

### Q15. Set Union and Intersection

Write a Python program using these two Sets:

```python
A = {2, 4, 6, 8, 10}
B = {6, 8, 10, 12, 14}
```

Perform the following tasks:

1. Find the union of A and B.
2. Find the intersection of A and B.
3. Print both results.
4. Print the number of elements in the union.

**Write your code below:**

```python
# Your code here
```

---
