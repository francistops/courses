def remove_nonints(nums):
    int_num = []
    for num in nums:
        if type(num) is int:
            int_num.append(num)
    return int_num
