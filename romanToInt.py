def romanToInt( s: str):
    res = 0;
    obj = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    i = 0
    while i < len(s)-1:
        if(s[i] == "I" and s[i+1] == "V"):
            res += 4
            i+=1
        elif(s[i] == "I" and s[i + 1] == "X"):
            res += 9
            i+=1
        elif (s[i] == "X" and s[i + 1] == "L"):
            res += 40;
            i+=1
        elif (s[i] == "X" and s[i + 1] == "C"):
            res += 90;
            i+=1
        elif (s[i] == "C" and s[i + 1] == "D"):
            print(s[i],s[i+1])
            res += 400;
            i+=1
        elif (s[i] == "C" and s[i + 1] == "M"):
            res += 900;
            i+=1
        else:
            res += obj[s[i]];
        i+=1
        
    return res;
            
    
print(romanToInt("III"))
print(romanToInt('LVIII'))
print(romanToInt('MCMXCIV'))