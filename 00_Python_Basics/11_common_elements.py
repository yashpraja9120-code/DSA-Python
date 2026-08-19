#Write a function that takes 2 arrays and prints the members of the first
#array that are present in the second array. (HINT: use Membership
#Comprehension)

def common_members(arr1, arr2):
    result = [x for x in arr1 if x in arr2]
    print(result)


arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

common_members(arr1, arr2)