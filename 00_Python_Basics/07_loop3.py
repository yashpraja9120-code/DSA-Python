#Create an array that has user defined inputs and with the help of for loop,
#fetch all the prime numbers and print the numbers

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

for num in numbers:
    if num < 2:
        continue

    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)

   