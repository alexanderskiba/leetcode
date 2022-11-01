def romanToInt(s):
    """I can be placed before V (5) and X (10) to make 4 and 9. 
       X can be placed before L (50) and C (100) to make 40 and 90. 
       C can be placed before D (500) and M (1000) to make 400 and 900."""
    
    digits={"I": 1,
           "V": 5,
           "X": 10,
           "L": 50,
           "C": 100,
           "D": 500,
           "M": 1000}

    i = 0
    total = 0
    while i < len(s):
        s1 = digits[s[i]]
        if i+1 < len(s):
            s2= digits[s[i+1]]
            if s1 >=s2:
                total+= s1
                i+=1
            else:
                total -= s1
                i+= 1
        else:
            total += s1
            i+= 1
                
                
    return total
