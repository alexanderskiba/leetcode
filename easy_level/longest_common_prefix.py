def longestCommonPrefix(strs):
    s = strs[0]
    #берем первый элемент списка
    for i in range(1, len(strs)):
        # бежим по списку, не включая самый первй элемент
        # и проверяем наличие в оставшихся строках нашей подстроки  s
        # на каждой итерации убавляем от нашей подстроки одну букву и так проверяем пока подстрока не будет найдена
        # и так для каждого элемента
        while strs[i].find(s) != 0:
            s = s[:-1]
    return s
