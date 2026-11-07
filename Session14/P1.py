fruits=set() #Empty Set


#Methods : 
#1. add
fruits.add('Mango')
fruits.add('Banana')
fruits.add('Orange')

print(type(fruits))
print(fruits)

print("---------")

#2. remove
fruits.remove('Mango')
print(fruits)


#3. pop --> Pop removes any one random element
fruits.pop()
print(fruits)

A=set()
B=set()

A.add(1)
A.add(2)
A.add(5)
A.add(4)
A.add(3)

B.add(3)
B.add(5)
B.add(7)
B.add(8)
B.add(10)

union=A.union(B)
print("Union: ",union)

intersection=A.intersection(B)
print("Intersection:",intersection)
