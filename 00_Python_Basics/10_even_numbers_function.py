#Write a function to take an array and return another array that contains the
#members of the first array that are even
 
def even_numbers(arr):
    result = []

    for num in arr:
        if num % 2 == 0:
            result.append(num)

    return result


numbers = [10, 23, 4, 42, 75, 24, 54]

print(even_numbers(numbers))