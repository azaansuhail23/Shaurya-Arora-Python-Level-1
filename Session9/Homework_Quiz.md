# Python List Methods — Easy Quiz

**Topics:** `append()`, `extend()`, `len()`, `pop()`, `reverse()`, `count()`, `index()`

**Difficulty:** Easy
**Total Questions:** 20

---

## Question 1

What does the `append()` method do?

A. Removes an item from a list
B. Adds one item to the end of a list
C. Reverses a list
D. Counts items in a list

---

## Question 2

What will be the output?

```python
numbers = [1, 2, 3]
numbers.append(4)

print(numbers)
```

git A. `[4, 1, 2, 3]`
B. `[1, 2, 3]`
C. `[1, 2, 3, 4]`
D. `[4]`

---

## Question 3

What will be the output?

```python
colors = ["red", "blue"]
colors.append("green")

print(colors)
```

A. `["green", "red", "blue"]`
B. `["red", "blue", "green"]`
C. `["red", "green"]`
D. `["blue", "green"]`

---

## Question 4

What does `extend()` do?

A. Adds multiple items to a list
B. Removes the last item
C. Reverses the list
D. Finds an item's position

---

## Question 5

What will be the output?

```python
a = [1, 2]
b = [3, 4]

a.extend(b)

print(a)
```

A. `[1, 2]`
B. `[3, 4]`
C. `[1, 2, 3, 4]`
D. `[1, 2, [3, 4]]`

---

## Question 6

What is the output?

```python
fruits = ["apple", "banana", "mango"]

print(len(fruits))
```

A. `2`
B. `3`
C. `4`
D. `1`

---

## Question 7

What does `len()` tell us?

A. The first item of a list
B. The last item of a list
C. The number of items in a list
D. The position of an item

---

## Question 8

What will happen here?

```python
numbers = [10, 20, 30]
numbers.pop()

print(numbers)
```

A. `[10, 20]`
B. `[20, 30]`
C. `[10, 30]`
D. `[10, 20, 30]`

---

## Question 9

Which item is removed when we use `pop()` without giving an index?

```python
animals = ["cat", "dog", "rabbit"]
animals.pop()
```

A. `"cat"`
B. `"dog"`
C. `"rabbit"`
D. All items

---

## Question 10

What will be the output?

```python
numbers = [1, 2, 3, 4]
numbers.pop(1)

print(numbers)
```

A. `[1, 3, 4]`
B. `[2, 3, 4]`
C. `[1, 2, 4]`
D. `[1, 2, 3]`

---

## Question 11

What does the `reverse()` method do?

A. Sorts the list
B. Deletes the list
C. Reverses the order of items
D. Counts the items

---

## Question 12

What will be the output?

```python
numbers = [1, 2, 3, 4]
numbers.reverse()

print(numbers)
```

A. `[1, 2, 3, 4]`
B. `[4, 3, 2, 1]`
C. `[2, 3, 4, 1]`
D. `[4, 1, 2, 3]`

---

## Question 13

What does the `count()` method do?

A. Counts how many times a particular value appears
B. Counts only the first item
C. Removes repeated items
D. Reverses the list

---

## Question 14

What will be the output?

A. `1`
B. `2`
C. `3`
D. `5`

---

## Question 15

What will be the output?

```python
fruits = ["apple", "banana", "apple", "mango"]

print(fruits.count("apple"))
```

A. `1`
B. `2`
C. `3`
D. `4`

---

## Question 16

What does the `index()` method help us find?

A. The number of items
B. The position of an item
C. The last item
D. The size of the list

---

## Question 17

What will be the output?

```python
colors = ["red", "blue", "green"]

print(colors.index("blue"))
```

A. `0`
B. `1`
C. `2`
D. `3`

---

## Question 18

What will be the output?

```python
animals = ["cat", "dog", "fish", "bird"]

print(animals.index("fish"))
```

A. `1`
B. `2`
C. `3`
D. `4`

---

## Question 19

Which method would you use to add **one item** to the end of a list?

A. `extend()`
B. `append()`
C. `pop()`
D. `reverse()`

---

## Question 20

Which method would you use to count how many times `"apple"` appears in a list?

```python
fruits = ["apple", "banana", "apple", "mango"]
```

A. `fruits.len("apple")`
B. `fruits.index("apple")`
C. `fruits.count("apple")`
D. `fruits.pop("apple")`

---

# Answer Key


| Question | Answer |
| ---------- | -------- |
| 1        | B      |
| 2        | C      |
| 3        | B      |
| 4        | A      |
| 5        | C      |
| 6        | B      |
| 7        | C      |
| 8        | A      |
| 9        | C      |
| 10       | A      |
| 11       | C      |
| 12       | B      |
| 13       | A      |
| 14       | C      |
| 15       | B      |
| 16       | B      |
| 17       | B      |
| 18       | B      |
| 19       | B      |
| 20       | C      |

---

# Quick Revision


| Method      | Purpose                       | Example                  |
| ------------- | ------------------------------- | -------------------------- |
| `append()`  | Adds one item to the end      | `numbers.append(5)`      |
| `extend()`  | Adds multiple items           | `numbers.extend([5, 6])` |
| `len()`     | Finds number of items         | `len(numbers)`           |
| `pop()`     | Removes and returns an item   | `numbers.pop()`          |
| `reverse()` | Reverses the list             | `numbers.reverse()`      |
| `count()`   | Counts occurrences            | `numbers.count(5)`       |
| `index()`   | Finds the position of an item | `numbers.index(5)`       |
