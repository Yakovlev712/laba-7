nums = list(map(int, input("Введи мне числа").split()))
jumps = 0
end = 0
far = 0

for i in range(len(nums) - 1):
    far = max(far, i + nums[i])

    if i == end:
        jumps += 1
        end = far

print('количество прыжков ',jumps)
