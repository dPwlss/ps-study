A, B, C, M = map(int, input().split())
P, hour, work = 0, 0, 0

while hour != 24:
    hour += 1
    
    if P + A <= M:
        P += A
        work += B
        
    else:
        if P > M:
            work = 0
            break
        else:
            P -= C
            if P < 0:
                P = 0
print(work)
