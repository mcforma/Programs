'''
Question 1: For each of the following statements, write the EXACT output if you were to run them in IDLE. 
You'll learn more if you write what you think the output is and later actually testing them.
 
a)	3 + 4 * 10 % 2 + 4 / 2 - 1

b)	3 % 5 + 6 // 5 + 4 * 7 + 9 - 5

c)	for m in range(1, 10, 2):
    print(m**2)

d)	for q in range(-1, -10):
    print(q)

e)	for num in [-1, 27, 12, 22]:
    print(num + 2)
 
f)	print("This", "is ", "an exam\nreview")

g)	print("One", "Two", "Three", sep="\t", end="...\n")

h)	label = "numbers"
print(f"The {label} are {912.83453727:0.5f}, {31.4159265:0.5}, {12.89}, and {12}")


Question 2: a) What is 73 in binary? 
            b) What is 110010 in decimal?


'''

# 1. a) 3 + 4 * 10 % 2 + 4 / 2 - 1
# 4*10 = 40 % 2 = 0 
# 3 + 0 + 2 - 1 = 4
# Technically this will output nothing because there is no print statement. But the answer is 4.
print()
print(3 + 4 * 10 % 2 + 4 / 2 - 1)

# 1. b) 3 % 5 + 6 // 5 + 4 * 7 + 9 - 5 
# 3 % 5 = 3 + 
# 6 // 5 = 1 + 
# 4 * 7 = 28 +
# 9 - 5 = 4
# 3 + 1 + 28 + 4 = 36
# Technically this will output nothing because there is no print statement. But the answer is 36.
print()
print(3 % 5 + 6 // 5 + 4 * 7 + 9 - 5 )

# 1. c) for m in range(1, 10, 2):
#           print(m**2)
# 1
# 9
# 25
# 49
# 81
print()

for m in range(1, 10, 2):
    print(m**2)

#= 1. d) for q in range(-1, -10):
#           print(q)
# This will print nothing because it is out of range. Default step is 1.
# For this to function, the step size would have to be negative
print()

for q in range(-1, -10):
    print(q)


# 1. e) for num in [-1, 27, 12, 22]:
#           print(num + 2)
# 1
# 29
# 14
# 24
print()

for num in [-1, 27, 12, 22]:
    print(num + 2)

# 1. f) print("This", "is ", "an exam\nreview")
# This is  an exam
#review
# commas in print statements after quotes automatically add spaces.... Don't forget
print()
print("This", "is ", "an exam\nreview")


# 1. g)	print("One", "Two", "Three", sep="\t", end="...\n")
# One   Two     Three...
print()
print("One", "Two", "Three", sep="\t", end="...\n")


# 1. h) label = "numbers"
#       print(f"The {label} are {912.83453727:0.5f}, {31.4159265:0.5}, {12.89}, and {12}")
# The numbers are 912.83454, 31.41593, 12.89 and 12

print()
label = "numbers"
print(f"The {label} are {912.83453727:0.5f}, {31.4159265:0.5}, {12.89}, and {12}")


# 2. a) What is 73 in binary? 1001001
# 2. b) What is 110010 in decimal? 50

