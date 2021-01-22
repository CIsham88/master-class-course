empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
# ^ this is a list of int's, sorted
print(sorted_numbers)
print(numbers)

digits = sorted("432985617")
# ^ this is a list of strings, sorted
# check the output when running the above code to see the difference
# alternatively, you could do this:
digitz = list("432985617")
print(digits)
print("-" * 10)
print(digitz)

more_numbers = list(numbers)
print(more_numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)
# These are not the same list, but both contain the same data
# you can also create a new list using a slice:
# more_numbers = numbers[:]
# this, however, would be the most efficient way to create a new list
# by copying the other:
# more_numbers = numbers.copy()