#Create 1st tuple with values -> (10, 20, 30), 2nd tuple with values -> (40,
#50, 60):

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

# a. Concatenate the two tuples
t_combine = tuple1 + tuple2
print("a.", t_combine)

# b. Repeat the elements 3 times
print("b.", t_combine * 3)

# c. Access the 3rd element
print("c.", t_combine[2])

# d. Access the first three elements
print("d.", t_combine[:3])

# e. Access the last three elements
print("e.", t_combine[-3:])
