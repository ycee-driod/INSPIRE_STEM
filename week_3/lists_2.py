friends = ["leon", "Abigael", "fidelis", "bridget", "kriss"]
for friend in friends:
    print(friend)

enemies = friends[:]

enemies = friends[:] #copy one list into another
print(enemies)

fruits = ["mango", "guava", "apple", "banana", "pineapple"]

# slice part of lists # index to (:) index...e.g[0:3]
print(fruits[0:3])   

del fruits[0]
print(fruits)

squares = [] # initializes an empty list
for x in range(0,11):
    squares.append(x**2)
print(squares)   



