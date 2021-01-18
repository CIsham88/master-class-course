
snake_types = open("texttest1.txt", "w")
# r = read
# r+ = read and write
# a = append(add)
# w = write(will completely overwrite and replace the file contents with whatever you add)

# print(snake_types.readline()) - reads first line
# print(snake_types.readline()) - reads second line
# alternative method would be ".readlines()" - can use [] to read line

# for snake in snake_types.readlines():
#     print(snake)
#
# # print(snake_types.readlines())
#
# snake_types.close()


snake_types.write("\nDiamondback")

snake_types.close()