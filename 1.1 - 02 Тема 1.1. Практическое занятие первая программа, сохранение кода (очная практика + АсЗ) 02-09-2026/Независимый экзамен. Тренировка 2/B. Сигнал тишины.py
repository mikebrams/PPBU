nums = list(map(int, input().split()))

for i in range(len(nums)):
    # print(nums[i : i + 2])

    if nums[i : i + 2] == [0, 0]:
        print(sum(nums[:i]))
        break





# разобраться - 9 // 5
# разобраться - 9 % 5
#