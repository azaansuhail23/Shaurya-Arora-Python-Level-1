# Python Tuple Homework

**Topic:** Tuples in Python
**Level:** Beginner
**Total Questions:** 15

## Part 1: Basic Concepts

### Q1. What is a tuple in Python?

A collection of similar or different data types. It is immutable.

### Q2. Write any three properties of a tuple.

- Immutable
- Ordered
- Indexing

### Q3. Which brackets are commonly used to create a tuple?

- A) `[]`
- B) `()` ✅
- C) `{}`
- D) `<>`

### Q4. What is the difference between a list and a tuple?

- List is mutable while tuple is immutable.

### Q5. True or False

A tuple is immutable, meaning its existing elements cannot be reassigned. ✅

## Part 2: Predict the Output

### Q6. What will be the output?

```python
numbers = (10, 20, 30, 40)
print(numbers[0])   Output : 10 ✅
```

### Q7. What will be the output?

```python
fruits = ("apple", "banana", "mango")
print(fruits[2])  Output : mango ✅
```

### Q8. What will be the output?

```python
numbers = (5, 10, 15, 20, 25)
print(numbers[1:4])  Output :  10 15 20
```

### Q9. What will be the output?

```python
colors = ("red", "green", "blue", "yellow")
print(colors[-1]) Output : yellow ✅
```

### Q10. What will happen when you run this code?

```python
numbers = (10, 20, 30)
numbers[1] = 50
print(numbers)
```

## Part 3: Write Python Programs

### Q11. Create a tuple containing five of your favorite fruits and print the tuple.

```Python
favourite_fruits = ('Orange', 'Banana','Grapes', 'Avacado', 'Mango')

print(favourite_fruits)
```

### Q12. Create a tuple containing five numbers. Print the first and last elements using indexing.

```Python
tup=(1,  2,  3,  4,  5)
#pos  0   1   2   3   4
#neg -5 -4  -3 -2  -1



#fetching the fast element
print(tup[0])  # positive indexing
print(tup[-5]) # negative indexing

#fetching the last element
print(tup[4])  # positive indexing
print(tup[-1])  # negative indexing


```

### Q13. Create the following tuple and print only the elements `20`, `30`, and `40` using slicing.

```python
numbers = (10, 20, 30, 40, 50)
#indexing     0    1    2    3    4

print(numbers[1:4])
```

### Q14. Create a tuple containing five colors and print the first three elements using slicing.

### Q15. Create a tuple containing your name, age, and favorite programming language. Print each element separately using indexing.

---
