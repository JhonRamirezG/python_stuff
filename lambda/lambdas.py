from functools import reduce


# One argument lambda
def add10(x): return x + 10


# Multy argument lambda
def mult(x, y): return x * y


# Use of lambda to sort by the index 1 (sorted).
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D)
print(points2D_sorted)

# Use of lambda to multiply each value of a list
a = [1, 2, 3, 4]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
