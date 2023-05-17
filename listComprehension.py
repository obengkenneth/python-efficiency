# a list of numbers using list comprehension
number = int(input("Enter a number from 0 to 100: "))
nums = [i for i in range(1, 101) if i % number == 0]
print(nums)