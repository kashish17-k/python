'''Write a Python program that accepts an integer (n) and
computes the value of n+nn+nnn'''

n = input("Enter an integer: ")


result = int(n) + int(n*2) + int(n*3)

print("Result:", result)