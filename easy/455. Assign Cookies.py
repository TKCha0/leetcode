g = [10,9,8,7]
s = [5,6,7,8]
g.sort(reverse=1)
s.sort(reverse=1)
kid = 0
cookie = 0
ans = 0
while kid < len(g) and cookie < len(s):
    if s[cookie] < g[kid]:
        kid += 1
    else:
        cookie += 1
        kid += 1
        ans += 1
    
    
 