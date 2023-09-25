# 백준 2309 - 일곱 난쟁이
import sys 
input = sys.stdin.readline 

h = [int(input()) for _ in range(9)]
h.sort()
total = sum(h)

for i in range(len(h)):
    for j in range(i+1, len(h)):
        if total - h[i] - h[j] == 100:
            h[i], h[j] = 0, 0
            for i in h:
                if i != 0:
                    print(i)
            exit()

 