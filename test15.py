def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        rom_to_int={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s = s[::-1]
        sum = rom_to_int[s[0]]
        for i in range(1,len(s)):
            if rom_to_int[s[i]] >= rom_to_int[s[i-1]]:
                sum = sum + rom_to_int[s[i]]
            else:
                sum = sum - rom_to_int[s[i]]
        return sum

rom = ['XI','IX','MCMXCIV']
for i in range(0,len(rom)):
    print(romanToInt(rom[i]))