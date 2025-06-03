def two_sum(numbers, target):
    seen = {}
    for num in numbers:
        diff = target - num
        if diff in seen:
            return [seen[diff], num]
        seen[num] = num