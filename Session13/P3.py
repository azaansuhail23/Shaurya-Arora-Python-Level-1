fruits={
    'Mango':5,
    'Banana':3,
    'Guava':2
}

print(fruits['Mango']) #Note --> This is much easier
print(fruits.get('Mango'))

print(fruits['Banana'])
print(fruits['Guava'])

#Property : .items   --> Learn It --> It will give you the list of key value pairs

print("-----------")

print(fruits.items())

print(fruits.pop('Guava')) #It remove the key and its value 

print("-----------")
print(fruits)