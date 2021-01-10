import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

for _ in range(int(input())):
	n = int(input())
	array = list(map(int, input().strip().split()))
	for i in range(1, len(array)):
		j = i
		while j > 0 and array[j] < array[j-1]:
			array[j], array[j-1] = array[j-1], array[j]
			j -= 1
	print(array)
