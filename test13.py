def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            is_neg = False
        elif x < 0:
            is_neg = True
        else:
            return 0
        
        if is_neg:
            reverse = '-' + str(x * -1)[::-1]
        else:
            reverse = str(x)[::-1]

        reverse_int = int(reverse)
        
        if reverse_int > 2**31 or reverse_int < -2**31:
            return 0

        return reverse_int

num = int(input('please input a num:'))
print('reversed num:', reverse(num))