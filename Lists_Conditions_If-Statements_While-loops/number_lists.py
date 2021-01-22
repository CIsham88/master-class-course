even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()
print(len(even))
print(len(odd))

print()
print("Mississippi".count("iss"))
print("_" * 10)
print()


even.extend(odd)
print(even)
another_even = even
print(another_even)
even.sort()

print()

print(even)
even.sort(reverse=True)
print(even)
print(min(odd))
print(sum(even))
another_even.remove(min(even))
print()

even.sort()
print(another_even)
even.insert(0, 1)
print(even)
