
lucky_numbers = [3, 7, 16, 27, 33]
friends = ["Cody", "Derek", "Kyle", "Tony", "Joe"]
# friends.extend(lucky_numbers)
friends.append("Leo")
friends.extend(["Ody", "Moo", "Matti G"])
print()

print(friends)
friends.insert(5, "James")
print()
print(friends)
print()
friends.insert(0, "William")
# ^this placed a new 'friend' named "William" at the beginning of the list (place 0)
print(friends)
print()
friends.remove("William")
# friends.clear = this will clear all contents from the  list
# friends.pop = will remove the last item from the list
print(friends)
print()

print(lucky_numbers)
# lucky_numbers.extend(friends)
print(lucky_numbers)

print()
print(friends.index("Cody"))
print(friends.count("Leo"))
friends.sort()
print(friends)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
friends2.extend(lucky_numbers)
print(friends2)