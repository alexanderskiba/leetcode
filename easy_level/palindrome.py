def isPalindrome(self, num):
        """
        :type x: int
        :rtype: bool
        """
        original_num = num
        revert = 0
        while num > 0:
            # находим остаток - последнюю цифру
            digit = num % 10
            # делим нацело - удаляем последнюю цифру
            num = num // 10
            # увеличиваем разрядность второго числа
            revert = revert * 10
            # добавляем очередную цифру
            revert = revert + digit
        if original_num == revert:
            return True
        else:
            return False
