s = "MCMXCIV"
roman = {"I" : 1 , "V" : 5 , "X" : 10 , "L" : 50
         , "C" : 100 , "D" : 500 , "M" : 1000}
a = 0
for i in range(len(s)):
    if i == len(s)-1 or roman.get(s[i]) >= roman.get(s[i+1]) :
        a += roman.get(s[i])
    else:
        a -= roman.get(s[i])










