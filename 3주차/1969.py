n, m = map(int, input().split())
DNA = []
for _ in range(n):
    DNA.append(input())
    
    
cnt = 0
result = ''
for i in range(m):
    count = [0, 0, 0, 0]
    for j in range(n):
        if DNA[j][i] == 'A':
            count[0] += 1
        elif DNA[j][i] == 'C':
            count[1] += 1
        elif DNA[j][i] == 'G':
             count[2] += 1
        elif DNA[j][i] == 'T':
            count[3] += 1
    idx = count.index(max(count))
    if idx == 0:
        result += 'A'
    elif idx == 1:
        result += 'C'
    elif idx == 2:
         result += 'G'
    elif idx == 3:
        result += 'T'
    cnt += n - max(count)

print(result)
print(cnt)
