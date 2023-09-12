# 백준 1747 - 소수&팰린드롬
import sys
input = sys.stdin.readline
import math

N = int(input())

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
    	if n % i == 0:
            return False
	return True
	
def is_pallindrome(n):
	for i in range(0, len(n)//2):
		if n[i] == n[-i]:
			continue
		else:
			return False
	return True

while(True):
	if is_pallindrome(N) and is_prime(N):
		break
	else:
		N += 1
		
print(N)