def twoSum(nums, target):
    """
    Решение за O(n)
    Из таргерта отнимаем элемент массива, получаем второе слагаемое,
    если элемент массиова есть в хештаблице, вернем индекс этого элемента и индекс второго слагаемого
    записываем элемент массива в хеш таблицу
    """
    sums = []
    hashTab = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashTab:
            return[nums.index(complement), i]
        hashTab[nums[i]] = nums[i]
