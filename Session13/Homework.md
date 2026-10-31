
# Python Dictionary Quiz – Basic Level

**Total Questions:** 15
**Difficulty:** Beginner
**Topics:** Dictionary creation, accessing values, updating values, `items()`, `keys()`, `values()`, `pop()`, `len()`, and loops.

---

# Section A: Multiple Choice Questions (10 MCQs)

### Q1. What is a dictionary in Python?

A. A collection of key-value pairs
B. A collection of only numbers
C. A collection of duplicate values only
D. A collection of characters

### Q2. Which brackets are used to create a dictionary in Python?

A. `( )`
B. `[ ]`
C. `{ }`
D. `< >`

### Q3. What will be the output?

```python
student = {'name': 'Ali', 'age': 12}
print(student['name'])
```

A. 12
B. Ali
C. name
D. student

### Q4. How do you access the age of a student?

```python
student = {'name': 'Ali', 'age': 12}
```

A. `student(age)`
B. `student[age]`
C. `student['age']`
D. `student.age`

### Q5. What does the `items()` method return?

A. Only dictionary keys
B. Only dictionary values
C. Key-value pairs
D. The number of items

### Q6. What will be printed?

```python
marks = {'Math': 90, 'English': 80}
print(marks.items())
```

A. `dict_items([('Math', 90), ('English', 80)])`
B. `['Math', 'English']`
C. `[90, 80]`
D. `2`

### Q7. What does the `pop()` method do in a dictionary?

A. Adds a new key
B. Removes a specified key and returns its value
C. Displays all keys
D. Sorts dictionary values

### Q8. What will be the output?

```python
fruits = {'apple': 10, 'mango': 20}
fruits.pop('apple')
print(fruits)
```

A. `{'apple': 10}`
B. `{'mango': 20}`
C. `{'apple': 10, 'mango': 20}`
D. `20`

### Q9. Which method is used to get all the keys from a dictionary?

A. `items()`
B. `values()`
C. `keys()`
D. `pop()`

### Q10. What will be the output?

```python
student = {'name': 'Ali', 'age': 12}
student['age'] = 13
print(student)
```

A. `{'name': 'Ali', 'age': 12}`
B. `{'name': 'Ali', 'age': 13}`
C. `{'age': 13}`
D. Error

---

# Section B: Small Python Programming Questions (5 Programs)

**Instructions:** Write Python programs for the following questions. Try to solve them yourself.

### Q11. Create a Dictionary

Create a dictionary named `student` containing the following information:

- Name: Ali
- Age: 12
- Class: 7
- City: Delhi

Print the complete dictionary.

**Expected Output:**

```text
{'name': 'Ali', 'age': 12, 'class': 7, 'city': 'Delhi'}
```

### Q12. Access Dictionary Values

Create the following dictionary:

```python
student = {
    'name': 'Ali',
    'age': 12,
    'class': 7
}
```

Write a program to print:

1. Student name
2. Student age
3. Student class

**Expected Output:**

```text
Ali
12
7
```

### Q13. Add and Update Dictionary Items

Create a dictionary:

```python
student = {
    'name': 'Ali',
    'age': 12
}
```

Perform the following operations:

1. Add a new key `city` with value `Delhi`.
2. Update the age from 12 to 13.
3. Print the updated dictionary.

**Expected Output:**

```text
{'name': 'Ali', 'age': 13, 'city': 'Delhi'}
```

### Q14. Use the items() Method

Create the following dictionary:

```python
fruits = {
    'apple': 10,
    'mango': 20,
    'banana': 30
}
```

Use the `items()` method and a `for` loop to print every fruit and its quantity.

**Expected Output:**

```text
apple 10
mango 20
banana 30
```

### Q15. Use the pop() Method

Create the following dictionary:

```python
mobile = {
    'brand': 'Samsung',
    'model': 'M36',
    'price': 15000
}
```

Perform the following operations:

1. Remove the `model` key using `pop()`.
2. Print the removed value.
3. Print the updated dictionary.

**Expected Output:**

```text
M36
{'brand': 'Samsung', 'price': 15000}
```

---
