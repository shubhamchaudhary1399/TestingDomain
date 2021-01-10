import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


x = int(input())
ans = 0
while x != 0:
    no = x % 10
    x = x//10
    ans = ans*10 + no
    print(ans)
print(ans)

