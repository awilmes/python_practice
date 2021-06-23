# Return distinct values from a list including duplicates (i.e. "1 3 5 3 7 3 1 1 5" -> "1 3 5 7")
# Return distinct values and their counts (i.e. the list above becomes "1(3) 3(3) 5(2) 7(1)")

nums = [1, 3, 5, 3, 7, 3, 1, 1, 5]

for i in set(nums):
    print(i,"({})".format(nums.count(i)))
