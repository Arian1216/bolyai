s = "93011NULL                5011005874          A0000000000010000000000001JKL00000000NULL                                              00000000A63"

d = [5,20,20,1,16,9,3,8,50,8,1,2]

start = 0
for x in d:
    print(s[start:x])
    start += x