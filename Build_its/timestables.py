for i in range(1, 13):
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(j, i, i * j))
print("----------")

    # what would happen if you indent line 4 once more, and what would happen if you removed the indent entirely
    # I belive if you indent line 4 once more the dashes will print between every single line for j
    # With the indent removed and aligning with line 1, I believe the dashes will be at the beginning of the program only
    # answer: i was right about the first, wrong about the second. the dashes were only at the END, not the beginning